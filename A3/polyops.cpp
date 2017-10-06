//Copyright 2017 Sihan Wang shwang95@bu.edu

#include <vector>

using namespace std;

typedef vector<double> Poly;

Poly add_poly(const Poly &a, const Poly &b) {
  Poly c;

  for(int i = 0; i < a.size() || i < b.size(); i++) //Calculate until the longer one of both vector's end
    c.push_back(a[i] + b[i]); //Add

  //Drop 0s at the end of vectors

  int i = c.size() - 1;

  while(c.size() > 1) {
    if(c[i] == 0) // If all 0, maintain last 0
      c.pop_back();
    else
      break;
    i--;
  }

  return c;
}

Poly multiply_poly(const Poly &a, const Poly &b) {
  const size_t M = a.size();
  const size_t N = b.size();

  Poly x = a;
  Poly h = b;
  Poly c(M + N - 1);

  //Convolution

  for(int i = M; i < M + N - 1; i++) //Adding 0s for convolve
    x.push_back(0);
  for(int i = N; i < M + N - 1; i++) //Adding 0s for convolve
    h.push_back(0);
  for(int i = 0; i < M + N - 1; i++) {
    c[i] = 0;
    for(int j = 0; j <= i; j++)
      c[i] += (x[j] * h[i - j]);
  }

  //Drop 0s at the end of vectors

  int i = c.size() - 1;

  while(c.size() > 1) {
    if(c[i] == 0)
      c.pop_back();
    else
      break;
    i--;
  }

  return c;
}