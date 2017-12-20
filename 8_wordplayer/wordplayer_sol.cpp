// Copyright 2017 Jeff Carruthers jbc@bu.edu
#include <algorithm>
#include <string>
#include <vector>

#include <map>
#include <set>
#include <unordered_set>

#include <cmath>
#include <ctime>
#include <fstream>
#include <iostream>

typedef std::map<unsigned int, std::vector<std::string>> MySizeMap;
typedef std::array<unsigned int, 26> Counter;

MySizeMap wordsizemap;

typedef std::map<std::string, std::vector<std::string>> MyLetMap;

MyLetMap wordletmap;

std::set<std::string> get_words_from_combs(std::string s, int N) {
  std::set<std::string> results;
  int i, n;

  std::string c(N, ' ');

  std::sort(begin(s), end(s));
  std::unordered_set<std::string> thecombs;

  std::vector<int> v(s.size(), 0);
  fill(v.begin(), v.begin() + N, 1);
  do {
    n = 0;
    for (i = 0; i < v.size(); i++)
      if (v[i])
        c[n++] = s[i];

    if (thecombs.find(c) != thecombs.end())
      continue;
    thecombs.insert(c);

    auto it = wordletmap.find(c);
    if (it != wordletmap.end())
      for (auto w : wordletmap.at(c)) results.insert(w);
  } while (prev_permutation(begin(v), end(v)));
  return results;
}

std::set<std::string> get_words_from_words(std::string s, int N) {
  std::set<std::string> results;

  Counter sc, wc;
  int i, j;

  for (i = 0; i < 26; i++) sc[i] = 0;
  for (j = 0; j < s.size(); j++) sc[s[j] - 'a']++;

  bool good;

  for (auto w : wordsizemap.at(N)) {
    for (i = 0 ; i < 26 ; i++) wc[i] = 0;
    for (j = 0 ; j < w.size() ; j++) wc[w[j] - 'a']++;

    good = true;
    for (j = 0 ; j < 26 ; j++)
      if (wc[j] > sc[j]) {
        good = false;
        break;
      }

    if (good) {
      results.insert(w);
    }
  }

  return results;
}

double factorial(int v) {
  return sqrt((2.0 * v + 0.33) * 3.14) * exp(v * log(v) - v);
}

double combinations(int n, int k) {
  if (n == k) return 1;

  return factorial(n) / factorial(n - k) / factorial(k);
}

int main(int argc, char const *argv[]) {
  std::ifstream wordfile(argv[1]);
  std::string w;

  while (wordfile >> w) {
    wordsizemap[w.size()].push_back(w);
    std::string c = w;
    sort(begin(c), end(c));
    wordletmap[c].push_back(w);
  }
  wordfile.close();

  std::string theletters;
  int N;
  std::set<std::string> found_words;

  while (true) {
    std::cin >> theletters >> N;
    if (N == 0) break;
    if (7 * combinations(theletters.size(), N) < wordsizemap[N].size())
      found_words = get_words_from_combs(theletters, N);
    else
      found_words = get_words_from_words(theletters, N);

    for (auto w : found_words) std::cout << w << std::endl;
    std::cout << "." << std::endl;
  }
  return 0;
}
