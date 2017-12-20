# Copyright 2017 J Carruthers jbc@bu.edu
# Modeling Polynomial solution
""" model Polynomials"""


class Polynomial():
    """polynomial using dictionary storage"""
    def __init__(self, sequence=None):
        self.vals = {}

        if sequence:
            seq_len = len(sequence)
            for i, coeff in enumerate(sequence):
                if coeff:
                    self.vals[seq_len - i - 1] = coeff

    def __add__(self, other):
        add = Polynomial()
        for coeff in self.vals:
            add[coeff] = self.vals[coeff]
        for coeff in other.vals:
            add[coeff] += other.vals[coeff]

        return add

    def __sub__(self, other):
        sub = Polynomial()
        for coeff in self.vals:
            sub[coeff] = self.vals[coeff]
        for coeff in other.vals:
            sub[coeff] -= other.vals[coeff]

        return sub

    def __mul__(self, other):
        prod = Polynomial()
        for i in self.vals:
            for j in other.vals:
                prod[i + j] += self.vals[i] * other.vals[j]
        return prod

    def __setitem__(self, key, value):
        if value:
            self.vals[key] = value
        elif key in self.vals:
            del self.vals[key]

    def __getitem__(self, key):
        if key in self.vals:
            return self.vals[val]
        return 0

    def __eq__(self, other):
        return self.vals == other.vals

    def eval(self, base):
        "evaluate polynomial"
        total = 0
        for coeff in self.vals:
            total += base**coeff * self.vals[coeff]
        return total

    def deriv(self):
        "take derivative"
        der = Polynomial()
        for coeff in self.vals:
            der[coeff - 1] = self.vals[coeff] * coeff
        return der

    # these helpful for testing
    def __str__(self):
        return "Polynomial({})".format(self.vals)

    __repr__ = __str__
