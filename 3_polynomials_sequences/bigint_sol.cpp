// Copyright 2017  J Carruthers jbc@bu.edu
#include <vector>
#include <string>
using std::vector;
using std::string;

typedef string BigInt;

void shrink(vector<int> *p) {
  while (p->back() == 0 and p->size() > 1)
    p->pop_back();
}
vector<int> from_bigint(const BigInt &a) {
  vector<int> Av(a.size(), 0);

  for (int i = 0; i < a.size() ; i++)
    Av[a.size() - 1 - i] = a[i] - '0';

  return Av;
}

BigInt to_bigint(const vector<int>& v) {
  BigInt S(v.size(), ' ');

  for (int k = 0; k < v.size() ; k++)
    S[v.size() - 1 - k] = v[k] + '0';

  return S;
}


BigInt multiply_int(const BigInt &a, const BigInt &b) {
  vector<int> Av = from_bigint(a);
  vector<int> Bv = from_bigint(b);

  vector<int> prod(a.size() + b.size(), 0);

  // multiply.

  for (int i = 0; i < Av.size(); i++)
    for (int j = 0; j < Bv.size(); j++)
      prod[i + j] += Av[i] * Bv[j];

  // Carry over
  for (int j = 0; j < prod.size() - 1; j++)
    if (prod[j] > 10) {
      prod[j + 1] += prod[j] / 10;
      prod[j] = prod[j] % 10;
    }

  shrink(&prod);

  return to_bigint(prod);
}
