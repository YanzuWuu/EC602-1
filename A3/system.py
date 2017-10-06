# Copyright 2017 Sihan Wang shwang95@bu.edu

import numpy as np

x, h = np.array(input().split(' '), dtype = float), np.array(input().split(' '), dtype = float)

print(' '.join([str(np.convolve(x, h)[0])] + [str(i) for i in np.trim_zeros(np.convolve(x, h)[1:], 'b')]))