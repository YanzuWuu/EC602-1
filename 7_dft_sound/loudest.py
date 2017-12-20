# Copyright 2017 Sihan Wang shwang95@bu.edu
# Copyright 2017 Yutong Gao gyt@bu.edu
# Copyright 2017 Zisen Zhou jason826@bu.edu

from numpy import *
import scipy.io.wavfile as wavfile


def loudest_band(music, frame_rate, bandwidth):
    N = len(music)
    zero_index = abs(arange(-frame_rate / 2, frame_rate,
                            frame_rate / len(music))).argmin()
    band = int(bandwidth / (frame_rate / len(music)))
    sig_fft = fft.fftshift(fft.fft(music))
    sig_pwr = abs(sig_fft) ** 2

    pwr = {}
    for i in range(zero_index, N - band + 1):
        pwr[i] = sum(sig_pwr[i:i + band])
    max_index = max(pwr, key=pwr.get)

    ones = zeros(N)
    for i in range(
            max_index,
            max_index +
            band +
            1):
        ones[i] = 1
    for i in range(
            2 *
            zero_index -
            max_index -
            band,
            2 *
            zero_index -
            max_index +
            1):
        ones[i] = 1
    fft_filtered = ones * sig_fft

    time = fft.ifft(fft.ifftshift(fft_filtered))

    result = ((max_index - zero_index) * (frame_rate / len(music)),
              (max_index - zero_index + band) * (frame_rate / len(music)), time.real)

    return result


def main():
    frame_rate, music = wavfile.read('bach10sec.wav')

    (low, high, loudest) = loudest_band(music[:, 0], frame_rate, 75)

    print("low:     ", low)
    print("high:    ", high)
    print("loudest: ", loudest)


if __name__ == '__main__':
    main()
