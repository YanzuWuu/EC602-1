# Copyright 2017 J Carruthers jbc@bu.edu
""" implement the DFT using arrays"""
from numpy import zeros, exp, array, pi


def DFT(x):
    "simple direct implementation of the DFT"
    try:
        N = len(x)
        v = -1j * 2 * pi / N
        X = zeros((N, ), dtype='complex128')
        l = array(range(N))
        for k in range(N):
            X[k] = x @ exp(v * l * k)
        return X
    except:
        pass

    raise ValueError
