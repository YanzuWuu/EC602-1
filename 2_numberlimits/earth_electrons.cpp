// Copyright 2017 Sihan Wang shwang95@bu.edu

#include <iostream>
#include <cmath>
int main() {
	double earth_mass = 5.972e27;
	double mol_mass = 64;
	double avg_mol = 6.023e23;
	double elec_num = 8;
	double num = earth_mass / mol_mass;
	double elect_num = num * elec_num;
	double tb = pow(2, 40);
	double storage = elect_num * avg_mol / tb;
	double storage_min = storage * 0.9;
	double storage_max = storage * 1.1;
	std::cout << storage << std::endl;
	std::cout << storage_min << std::endl;
	std::cout << storage_max << std::endl;
}