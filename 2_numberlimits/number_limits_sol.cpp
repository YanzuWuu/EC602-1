//Copyright 2017 J Carruthers jbc@bu.edu
// Definitions:
// Rs = factor by which float is better than int at representing small numbers
// Rm = factor by which float is better than int at representing large numbers
// Ri = factor by which int is better than float at representing integers
//
// Formulas:
//
// Rs = 1 / smallest_float_greater_than_zero
// Rm = maximum_float_value / largest_int_value
//
// Ri = largest_int_value / N
// where N is the largest integer such that all integers 1,2,3,...,N can be
// represented without loss of accuracy by a float of this size.
//
// For "smallest float" use normal values, not subnormal/denormal.

#include <iostream>
#include <cstdint>
#include <cfloat>
#include <cmath>
#include <limits>
int main(){

  int64_t maxint_64 = pow(2,53);
  int32_t maxint_32 = pow(2,24);
  int16_t maxint_16 = pow(2,11);

  double Rs,Ri,Rm;

  Rs = pow(2,14);
  Rm = (double) (2-1/pow(2,10))*pow(2,15)  / INT16_MAX;
  Ri = (double) INT16_MAX / maxint_16;

  std::cout<< "16 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

  Rs = 1/FLT_MIN;
  Rm = FLT_MAX / INT32_MAX;
  Ri = (double) INT32_MAX / maxint_32;

  std::cout<< "32 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;


  Rs = 1.0/DBL_MIN;
  Rm = DBL_MAX / INT64_MAX;
  Ri = (double) INT64_MAX / maxint_64;

  std::cout<< "64 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

  return 0;
}