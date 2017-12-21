# Copyright 2017 Sihan Wang shwang95@bu.edu
# Copyright 2017 Yutong Gao gyt@bu.edu
# Copyright 2017 Zisen Zhou jason826@bu.edu
"""Duplicate finder"""
import sys
from os import listdir
import re
import hashlib
from skimage.io import imread
import numpy as np

FILE_TO_WRITE = sys.argv[1]

def sha256(filename):
    """Calculate SHA256"""
    file_read = open(filename, 'rb')
    sha = hashlib.sha256()
    sha.update(file_read.read())
    print(sha.hexdigest())
    file_read.close()


def pattern(pattern_bool):
    """Pattern recognition"""
    pattern_return = ""
    for i in pattern_bool:
        pattern_return += "1" if i else "0"
    pattern_sig = ""
    for i in range(0, len(pattern_return), 3):
        pattern_sig += pattern_return[::-1][i + 2]
        pattern_sig += pattern_return[::-1][i + 1]
        pattern_sig += pattern_return[::-1][i]
    return (pattern_return, pattern_sig)


RESULT = {}
for FILE_TO_READ in listdir():
    if FILE_TO_READ.endswith('.png'):
        img = imread(FILE_TO_READ)
        img_non_white_coordinates = np.where(img < [255, 255, 255])
        img_rotated_non_white = np.sort(img_non_white_coordinates[1])
        top = img_non_white_coordinates[0][0]
        bottom = img_non_white_coordinates[0][-1]
        left, right = img_rotated_non_white[0], img_rotated_non_white[-1]
        parallel_bool = np.zeros(3 * (right - left + 1), dtype=bool)
        vertical_bool = np.zeros(3 * (bottom - top + 1), dtype=bool)
        for row in img[top:bottom + 1, left:right + 1, :] == 255:
            parallel_bool = np.bitwise_xor(parallel_bool, row.flatten())
        for col in np.transpose(
                img[top:bottom + 1, left:right + 1, :], (1, 0, 2)) == 255:
            vertical_bool = np.bitwise_xor(vertical_bool, col.flatten())
        (parallel, parallel_sig) = pattern(parallel_bool)
        (vertical, vertical_sig) = pattern(vertical_bool)
        temp_set = frozenset([parallel, vertical, parallel_sig, vertical_sig])
        RESULT.setdefault(temp_set, []).append(FILE_TO_READ)
for k in RESULT:
    RESULT[k] = sorted(
        RESULT[k],
        key=lambda x: int(re.findall(r'\d+', x)[0]))
FILE = open(FILE_TO_WRITE, 'w')
for k in sorted(
        RESULT,
        key=lambda x: int(re.findall(r'\d+', RESULT[x][0])[0])):
    FILE.write(" ".join(RESULT[k]))
    FILE.write("\n")
FILE.close()
sha256(FILE_TO_WRITE)
