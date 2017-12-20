# Copyright 2017 Sihan Wang shwang95@bu.edu
# Copyright 2017 Yutong Gao gyt@bu.edu
# Copyright 2017 Zisen Zhou jason826@bu.edu

from numpy import zeros, exp, array, pi


def DFT(x):
    try:
        return exp(-2j * pi * array(range(len(x))) * array(range(len(x)))
                   [:, None] / len(x)) @ array(x, dtype=complex)
    except TypeError:
        raise ValueError
