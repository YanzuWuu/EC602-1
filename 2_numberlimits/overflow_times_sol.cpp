// Copyright 2017 J Carruthers jbc@bu.edu
#include <iostream>
#include <ctime>
#include <cmath>
#include <cstdint>


int main() {
  uint8_t m = 1;
  uint16_t i = 1;

  clock_t start_clock, end_clock;

  start_clock = clock();
  while (m > 0)
    m++;
  end_clock = clock();
  double seconds_int8 =
    static_cast<double>(end_clock - start_clock) / CLOCKS_PER_SEC;

  start_clock = clock();
  while (i > 0)
    i++;
  end_clock = clock();
  double seconds_int16 =
   static_cast<double>(end_clock - start_clock) / CLOCKS_PER_SEC;

  double seconds_int32 = seconds_int16 * pow(2, 16);

  std::cout << "estimated int8 time (nanoseconds): "
            << seconds_int16 / 256 * 1e9  << std::endl;
  std::cout << "measured int16 time (microseconds): "
            << seconds_int16 * 1e6 << std::endl;
  std::cout << "estimated int32 time (seconds): "
            << seconds_int32 << std::endl;
  std::cout << "estimated int64 time (years): "
            << seconds_int32 * pow(2, 32) / 365 / 60 / 60 / 24 << std::endl;
}
