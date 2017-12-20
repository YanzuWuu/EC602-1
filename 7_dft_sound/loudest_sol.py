# Copyright 2017 J Carruthers jbc@bu.edu
""" loudest solution
"""

from numpy import pi, cos, sin, linspace, fft, convolve, r_, ones


def loudest_band(music, frame_rate, bandwidth):
    N = music.shape[0]
    fmax = frame_rate / 2
    T = N / frame_rate
    F = fft.fft(music)
    df = 1/T
    f = df * r_[0:N//2]

    S = abs(F[:N//2])**2
    BW = int(bandwidth//df)
    R = convolve(S, ones((BW,)), mode='same')
    Rm = R.argmax()
    if Rm > BW//2:
        high = f[Rm + BW//2]
        low = f[Rm - BW//2]
    else:
        low = 0
        high = bandwidth

    f = fft.fftshift(df * r_[0:N] - fmax)
    G = F * (abs(f) >= low) * (abs(f) < high)
    g = fft.ifft(G).real

    return low, high, g
