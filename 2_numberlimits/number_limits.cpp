// Copyright 2017 Sihan Wang shwang95@bu.edu

#include <iostream>
#include <cstdint>
#include <cfloat>
#include <cmath>
#include <limits>

int main () {
	/*Binary16*/
	float float_b16_max = (2 - pow(2, -10)) * pow(2, 15); // Max half float number
	float float_b16_min = pow(2, -14); // Min half float number
	int int_b16_max = std::numeric_limits<int16_t>::max(); // Max half int number

	// Calculate Rs, Ri, and Rm for half/binary16 vs int16_t
	float Rs = 1 / float_b16_min;
	float Rm = float_b16_max / int_b16_max;
	float Ri = int_b16_max / pow(2, 11);
	
	// Print out
	std::cout << "16 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

	/*Binary32*/
	// Calculate Rs, Ri, and Rm for float/single/binary32 vs int32_t
	double Rs1 = 1 / std::numeric_limits<float>::min();
	double Rm1 = std::numeric_limits<float>::max() / std::numeric_limits<int32_t>::max();
	double Ri1 = std::numeric_limits<int32_t>::max() / pow(2, 24);

	//Print out
	std::cout<< "32 : Ri= "<< Ri1 << " Rm= " << Rm1 << " Rs= " << Rs1 << std::endl;

	/*Binary64*/
	// Calculate Rs, Ri, and Rm for double/binary64 vs int64_t
	long double Rs2 = 1 / std::numeric_limits<double>::min();
	long double Rm2 = std::numeric_limits<double>::max() / std::numeric_limits<int64_t>::max();
	long double Ri2 = std::numeric_limits<int64_t>::max() / pow(2, 53);

	//Print out
	std::cout << "64 : Ri= " << Ri2 << " Rm= " << Rm2 << " Rs= " << Rs2 << std::endl;

	return 0;
}
