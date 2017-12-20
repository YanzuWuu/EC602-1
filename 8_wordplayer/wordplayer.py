# Copyright 2017 Sihan Wang shwang95@bu.edu
# Copyright 2017 Yutong Gao gyt@bu.edu
# Copyright 2017 Zisen Zhou jason826@bu.edu

import sys
import itertools
import math


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


def contain(child, parent):
    temp = list(parent)
    for c in list(child):
        try:
            temp.remove(c)
        except ValueError:
            return 0
    return 1


words = open(sys.argv[1]).read().split()
wordSet = {}
for k in words:
    wordin = tuple(sorted(k))
    wordSet.setdefault(
        len(k), {
            wordin: []}).setdefault(
        wordin, []).append(k)

while(True):
    inline = input().split()
    n = int(inline[1])
    if n == 0:
        exit(0)
    lineSet = sorted(inline[0])
    result = []
    if(wordSet.get(n)):
        if(nCr(len(lineSet), n) > len(wordSet[n])):
            for i in wordSet[n]:
                if(contain(i, lineSet)):
                    for j in wordSet[n][i]:
                        result.append(j)
        else:
            combinations = list(set(itertools.combinations(lineSet, n)))
            for i in combinations:
                temp = tuple(i)
                if(temp in wordSet[n]):
                    for j in wordSet[n][temp]:
                        result.append(j)
    for i in sorted(set(result)):
        print(i)
    print('.')
