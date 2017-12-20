# Copyright 2017 J Carruthers jbc@bu.edu
# Modeling Polynomial solution
""" model Polynomials"""


class Polynomial(dict):
    """polynomial using dictionary storage"""

    def __init__(self, sequence=None):
        if sequence:
            coeffs = range(len(sequence) - 1, -1, -1)
            super().__init__(zip(coeffs, sequence))
            self.clean_zeros()

    def clean_zeros(self):
        keylist = list(self.keys())
        for coeff in keylist:
            if not self[coeff]:
                del self[coeff]

    def __add__(self, other):
        add = Polynomial()
        for coeff in self:
            add[coeff] = self[coeff]
        for coeff in other:
            add[coeff] += other[coeff]

        return add

    def __sub__(self, other):
        sub = Polynomial()
        for coeff in self:
            sub[coeff] = self[coeff]
        for coeff in other:
            sub[coeff] -= other[coeff]

        return sub

    def __mul__(self, other):
        prod = Polynomial()
        for i in self:
            for j in other:
                prod[i + j] += self[i] * other[j]
        return prod

    def __setitem__(self, key, value):
        if value:
            super().__setitem__(key, value)
        elif key in self:
            del self[key]

    def __getitem__(self, key):
        return super().get(key, 0)

    def eval(self, base):
        "evaluate polynomial"
        total = 0
        for coeff in self:
            total += base**coeff * self[coeff]
        return total

    def deriv(self):
        "take derivative"
        der = Polynomial()
        for coeff in self:
            der[coeff - 1] = self[coeff] * coeff
        der.clean_zeros()
        return der
