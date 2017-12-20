// Copyright 2017  J Carruthers jbc@bu.edu
#include <vector>

typedef std::vector<double> Poly;

void shrink(Poly *p) {
  while (p->back() == 0 and p->size() > 1)
    p->pop_back();
}

Poly add_poly_sh_lo(const Poly &shorter, const Poly &longer) {
  Poly sum(longer.size(), 0.0);

  for (int i = 0 ; i < shorter.size() ; i++)
    sum[i] = shorter[i] + longer[i];

  for (int i = shorter.size() ; i < longer.size() ; i++)
    sum[i] = longer[i];

  shrink(&sum);

  return sum;
}

Poly add_poly(const Poly &a, const Poly &b) {
  if (a.size() < b.size())
    return add_poly_sh_lo(a, b);
  else
    return add_poly_sh_lo(b, a);
}


Poly multiply_poly(const Poly & a, const Poly & b) {
  Poly prod(a.size() + b.size() - 1, 0);

  for (int i = 0; i < a.size(); i++)
    for (int j = 0; j < b.size(); j++)
      prod[i + j] += a[i] * b[j];

  shrink(&prod);

  return prod;
}
