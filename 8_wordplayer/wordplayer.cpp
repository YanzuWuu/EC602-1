// Copyright 2017 Sihan Wang shwang95@bu.edu
// Copyright 2017 Yutong Gao gyt@bu.edu
// Copyright 2017 Zisen Zhou jason826@bu.edu

#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>

int main(int argc, char const *argv[]) {
  std::ifstream infile;
  infile.open(argv[1]);
  std::string line, sorted_line;
  std::map<int, std::map<std::string, std::vector<std::string>>> words;
  while (std::getline(infile, line)) {
    sorted_line = line;
    sort(sorted_line.begin(), sorted_line.end());
    words[line.length()][sorted_line].push_back(line);
  }
  infile.close();

  std::string input;
  int length;
  while (true) {
    std::cin >> input >> length;
    if (length == 0)
      break;
    std::sort(input.begin(), input.end());
    std::vector<std::string> result;
    if (length == input.length()) {
      result = words[length][input];
    } else {
      int *p = new int[length];
      for (int i = 0; i < length; i++)
        p[i] = i;
      bool flag = true;
      while (flag) {
        std::string temp;
        for (int i = 0; i < length; i++)
          temp.push_back(input[p[i]]);
        std::vector<std::string> current = words[length][temp];
        result.insert(result.end(), current.begin(), current.end());
        for (int i = length - 1; i > -1; i--) {
          int stop = input.length() - length + i;
          int temp = p[i];
          p[i] = stop + 1;
          while (temp < stop) {
            temp++;
            if (input[temp] != input[temp - 1]) {
              p[i] = temp;
              break;
            }
          }
          if (p[i] > stop) {
            if (i == 0) {
              flag = false;
              break;
            }
          } else {
            for (int k = i + 1; k < length; k++)
              p[k] = p[k - 1] + 1;
            break;
          }
        }
      }
    }
    std::sort(result.begin(), result.end());
    for (auto &i : result)
      std::cout << i << std::endl;
    std::cout << "." << std::endl;
  }
  return 0;
}
