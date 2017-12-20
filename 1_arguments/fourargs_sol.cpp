// Copyright 2017 jbc@bu.edu
// Solution for fourargs.cpp
#include <iostream>
int main(int argumentcount,char const **arguments) {
 for (int i=1; i < argumentcount and i < 5; i++)
   std::cout << arguments[i] << '\n';
 for (int i=5; i < argumentcount ; i++)
   std::cerr << arguments[i] << '\n';
 return 0;
}