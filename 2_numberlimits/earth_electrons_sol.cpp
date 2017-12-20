//Copyright 2017 J Carruthers jbc@bu.edu
#include <iostream>
#include <cmath>

using namespace std;

int main(){

	double r=6371;

	double pi = 3.14159;
	double V = 4.0/3.0 * pi * pow(r*1000,3);

	double density = 0.007 * 1e6 ;
	double mass_earth = V * density;

	double u =  1.66e-27 ;
	double iron_mass = 56 * u;


	double num_iron_atoms = mass_earth /iron_mass;

	int electrons_per_atom = 26;
	double num_electrons = electrons_per_atom * num_iron_atoms;

	double earthTB = num_electrons /1e12/8;
	cout << earthTB << endl;
	cout << earthTB/2 << endl;
	cout << earthTB*10 << endl;

	return 0;
}