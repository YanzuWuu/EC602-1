// Copyright year Sihan Wang shwang95@bu.edu
#include <iostream>
int main (int argcont, char **arg) {
	for(int i=1;i<=4;i++) 
		std::cout << arg[i] << '\n';
	for(int j=5;j<=argcont;j++)
		std::cerr << arg[j] << '\n';
	return 0;
}