# Copyright 2017 J Carruthers jbc@bu.edu
import numpy
L = [[float(x) for x in input().split()] for i in range(2)]
print(str(numpy.convolve(L[0], L[1]))[1:-1])
