# Copyright 2017 J Carruthers jbc@bu.edu
import scipy.io.wavfile as wavfile
import numpy as np

def get_tones(digit):
    n = digit - 1 if digit else 10
    return [697,770,852,941][n//3],[1209,1336,1477,1633][n%3]

DTMF={str(s):get_tones(s) for s in range(10)}

def dialer(file_name,frame_rate,phone,tone_time,trigfcn=np.sin):
    N = int(frame_rate*tone_time)
    t = np.linspace(0,tone_time,N,endpoint=False)
    digits = len(phone)
    tones = np.empty( (digits,N) )
    for i in range(digits):
        low,high = DTMF[phone[i]]
        tones[i,:] = trigfcn(2*np.pi*low*t)+trigfcn(2*np.pi*high*t)
    thetones = tones.flatten()
    wavfile.write(file_name,data=thetones,rate=frame_rate)
    return thetones


DialerTests = ['6','19','321','147','258','963','9123456780','8675309','12223']

DialerTests2 = ['6178675309']

def main():
    for dig in DialerTests:
        dialer('dialer{}.wav'.format(dig),8000,dig,0.1)
    for dig in DialerTests2:
        dialer('dialer{}.wav'.format(dig),16000,dig,0.05)
if __name__ == '__main__':
    main()