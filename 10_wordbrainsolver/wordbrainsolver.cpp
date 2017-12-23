// Copyright 2017 Sihan Wang shwang95@bu.edu
// Copyright 2017 Yutong Gao gyt@bu.edu
// Copyright 2017 Zisen Zhou jason826@bu.edu

#include <stdlib.h>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#define ALPHABETS 26

typedef std::vector <std::vector <char>> Word;

struct node {
 public:
  char me;
  struct node *parent;
  struct node *children[ALPHABETS];
  std::string word = "";
  bool ep = false;
};

struct puzzle {
 public:
  int dimension = 0;
  Word board;
  void clear_board(int d);
  void display(int n);
};

int solve_controller(std::vector <std::string> puzzle_list, puzzle *puz,
                     node *trie,
                     std::vector <int> lengths,
                     std::map <int, char> sol,
                     std::vector <std::string> *words,
                     std::set <std::string> *solset);
node * root;
void puzzle::clear_board(int d) {
  dimension = d;
  board.clear();
  board.resize(dimension, std::vector <char> (d, 0));
}

bool load_puzzle(const int& puzzle_length,
                 const std::vector<std::vector <char>>& puzzle_words,
                 const std::vector <std::string>& puzzle_list,
                 std::vector <int> *lengths, puzzle *puz) {
  puz->clear_board(puzzle_length);
  for (int j = 0; j < puz->dimension; j++) {
    for (int i = 0; i < puzzle_words.size(); i++) {
      puz->board[j][i] = puzzle_words[puzzle_words.size() - 1 - i][j];
    }
  }
  for (auto &i : puzzle_list) {
    lengths->push_back(i.length());
  }
  if (lengths->size() == 0 || puz->dimension == 0)
    return false;
  return true;
}

int solve_puzzle(std::vector <std::string> puzzle_list, puzzle *puz,
                 std::vector <int> lengths,
                 node *trie,
                 std::map <int, char> *sol,
                 int cellx, int celly,
                 std::vector <std::string> *words,
                 std::set <std::string> *solset
                ) {
  if (!trie) return false;
  std::map <int, char> tsol;
  tsol.insert(sol->begin(), sol->end());
  (tsol)[cellx + celly * puz->dimension] = trie->me;
  for (const auto &p : (*sol))
    if (trie->ep) {
      std::vector <int> tlengths = lengths;
      tlengths.erase(tlengths.begin());
      std::vector <std::string> twords = *words;
      twords.push_back(trie->word);
      for (const auto &p : (twords))
        if (solve_controller(puzzle_list, puz, root, tlengths,
                             tsol, &twords, solset)) {
          *words = twords;
          *sol = tsol;
          return true;
        } else {
          return false;
        }
    }
  int minx = (cellx - 1 > 0) ? cellx - 1 : 0;
  int miny = (celly - 1 > 0) ? celly - 1 : 0;
  int maxx = (cellx + 1 < puz->dimension) ? cellx + 1 : puz->dimension - 1;
  int maxy = (celly + 1 < puz->dimension) ? celly + 1 : puz->dimension - 1;
  for (int x = minx; x <= maxx; x++) {
    for (int y = miny; y <= maxy; y++) {
      if (tsol.count(x + y * puz->dimension))
        continue;
      char c;
      try {
        c = puz->board.at(x).at(y);
      } catch(std::out_of_range) {
        continue;
      }
      if (trie->children[c - 'a']) {
        if (solve_puzzle(puzzle_list, puz, lengths,
                         trie->children[puz->board.at(x).at(y) - 'a'], &
                         tsol, x, y, words, solset)) {
          sol->insert(tsol.begin(), tsol.end());
          return true;
        }
      }
    }
  }
  return false;
}

int solve_controller(std::vector <std::string> puzzle_list, puzzle *puz,
                     node *trie,
                     std::vector <int> lengths,
                     std::map <int, char> sol,
                     std::vector <std::string> *words,
                     std::set <std::string> *solset) {
  if (lengths.size() == 0) {
    std::string sols = "";
    for (const auto &p : *words)
      sols += p + " ";
    solset->insert(sols);
    return false;
  }
  puzzle tpuz = *puz;
  for (std::map <int, char>::reverse_iterator it = sol.rbegin();
       it != sol.rend(); ++it) {
    tpuz.board[it->first % tpuz.dimension].erase(
      tpuz.board[it->first % tpuz.dimension].begin()
      + it->first / tpuz.dimension);
  }
  for (int x = 0; x < tpuz.board.size(); x++) {
    for (int y = 0; y < tpuz.board.at(x).size(); y++) {
      std::map <int, char> tsol;
      std::vector <std::string> twords = *words;
      std::string temp, hint;
      if (twords.size() != 0) {
        for (int i = 0; i < twords.size(); i++) {
          temp = twords[i];
          hint = puzzle_list[i];
          int count = 0;
          for (int j = 0; j < temp.size(); j++) {
            if (hint[j] != '*') {
              if (temp[j] == hint[j])
                count++;
            } else {
              count++;
            }
          }
          if (count != temp.size()) {
            return false;
          }
        }
      }
      if (trie->children[lengths.front()]) {
        if (solve_puzzle(puzzle_list, &tpuz, lengths,
                         trie->children[lengths.front()]->children[tpuz.
                             board.at(x).at(y) - 'a'],
                         &tsol, x, y, &twords, solset)) {
          *words = twords;
          return true;
        }
      }
    }
  }
  return false;
}

int load_dictionary(std::string fn, node *trie) {
  std::ifstream infile(fn);
  std::string s;
  int count;
  while (infile >> s) {
    if (s.length() > ALPHABETS)
      continue;
    count++;
    if (trie->children[s.length()] == NULL) {
      trie->children[s.length()] = new node;
      trie->children[s.length()]->parent = trie;
      trie->children[s.length()]->me = '0' + s.length();
    }
    node * traverse = trie->children[s.length()];
    for (auto c : s) {
      if (traverse->children[c - 'a'] == NULL) {
        traverse->children[c - 'a'] = new node;
        traverse->children[c - 'a']->parent = traverse;
        traverse->children[c - 'a']->me = c;
      }
      traverse = traverse->children[c - 'a'];
    }
    traverse->ep = true;
    traverse->word = s;
  }
  return count;
}

std::vector <std::string> split_string(const std::string& s,
                                       const std::string& c) {
  std::vector <std::string> v;
  std::string::size_type pos1, pos2;
  pos2 = s.find(c);
  pos1 = 0;
  while (std::string::npos != pos2) {
    v.push_back(s.substr(pos1, pos2 - pos1));
    pos1 = pos2 + c.size();
    pos2 = s.find(c, pos1);
  }
  if (pos1 != s.length())
    v.push_back(s.substr(pos1));
  return v;
}

int main(int argc, char **argv) {
  node trie = node();
  node ltrie = node();
  load_dictionary(argv[1], &trie);
  load_dictionary(argv[2], &ltrie);
  while (true) {
    puzzle puz = puzzle();
    Word puzzle_words;
    std::string puzzles;
    std::string line = "";
    while (std::cin) {
      if (std::cin.eof()) exit(0);
      getline(std::cin, line);
      if (line == "") exit(0);
      if (line.find("*") == std::string::npos) {
        std::vector<char> data(line.begin(), line.end());
        puzzle_words.push_back(data);
      } else {
        puzzles = line;
        break;
      }
    }
    int puzzle_length = puzzle_words[0].size();
    std::vector <std::string> puzzle_list = split_string(puzzles, " ");
    root = &trie;
    std::map <int, char> sol;
    std::vector <int> lengths;
    if (!load_puzzle(puzzle_length, puzzle_words, puzzle_list, &lengths, &puz))
      return false;
    std::vector<std::string> words;
    std::set<std::string> solset;
    solve_controller(puzzle_list, &puz, &trie, lengths, sol, &words, &solset);
    if (solset.size() == 0) {
      root = &ltrie;
      solve_controller(puzzle_list,
                       &puz, &ltrie, lengths, sol, &words, &solset);
    }
    for (const auto &p : solset)
      std::cout << p << std::endl;
    std::cout << "." << std::endl;
  }
}
