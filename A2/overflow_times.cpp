// Copyright 2017 Sihan Wang shwang95@bu.edu

#include <iostream>
#include <stdint.h>
#include <ctime>
#include <math.h>
int main () {
	clock_t start_clock, end_clock;
	uint16_t m = 1;
	start_clock = clock();
	while (m > 0) 
		m++;
	end_clock = clock();
	double seconds = (double) (end_clock - start_clock) / CLOCKS_PER_SEC;
	double single_seconds = seconds / (pow(2, 16) - 1);
	std::cout << "estimated int8 time (nanoseconds): " << single_seconds * 1e9 * pow(2, 8)<< std::endl;
	std::cout << "measured int16 time (microseconds): "	<< seconds * 1e6 << std::endl;
	std::cout << "estimated int32 time (seconds): " << seconds * pow(2, 16) << std::endl;
	std::cout << "estimated int64 time (years): " << seconds * pow(2, 48) / 31536000 << std::endl;
	return 0;
}
