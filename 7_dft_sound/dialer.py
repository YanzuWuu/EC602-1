# Copyright 2017 Sihan Wang shwang95@bu.edu
# Copyright 2017 Yutong Gao gyt@bu.edu
# Copyright 2017 Zisen Zhou jason826@bu.edu

from numpy import *
import scipy.io.wavfile as wavfile


def dialer(file_name, frame_rate, phone, tone_time):
    freq = {
        "1": (697, 1209),
        "2": (697, 1336),
        "3": (697, 1477),
        "4": (770, 1209),
        "5": (770, 1336),
        "6": (770, 1477),
        "7": (852, 1209),
        "8": (852, 1336),
        "9": (852, 1477),
        "0": (941, 1336)}
    t = linspace(0, tone_time, int(frame_rate * tone_time), endpoint=False)
    outputWav = array([])
    for i in str(phone):
        outputWav = concatenate(
            (outputWav, sin(2 * pi * freq[i][0] * t) + sin(2 * pi * freq[i][1] * t)))
    wavfile.write(file_name, frame_rate, outputWav.astype(float32))
