# Copyright 2017  J Carruthers jbc@bu.edu
"solution for wordplayer.py"

import itertools
import sys


class LetterCount():
    "counter for letter spelling"
    def __init__(self, word):
        self.lets = [0]*26
        for let in word:
            self.lets[ord(let)-97] += 1

    def contains(self, other):
        "does self contain other"
        for let_s, let_o in zip(self.lets, other.lets):
            if let_o > let_s:
                return False
        return True

    def len(self):
        "extra"
        return len(self.lets)


def get_words_from_letters(letters, wordlen):
    "which words can be formed from wordlen and letters pile"
    result_words = set()
    if len(letters) < 12 or wordlen < 3 or len(letters)-wordlen < 3:
        for key in itertools.combinations(sorted(letters), wordlen):
            for word in DC.get(key, []):
                result_words.add(word)
    else:
        ourletters = LetterCount(letters)
        for word in D.get(wordlen, []):
            if ourletters.contains(D[wordlen][word]):
                result_words.add(word)

    return sorted(result_words)


if __name__ == "__main__":
    D, DC = {}, {}

    for w in open(sys.argv[1]).read().splitlines():
        if len(w) not in D:
            D[len(w)] = dict()
        D[len(w)][w] = LetterCount(w)

        k = tuple(sorted(w))
        if k in DC:
            DC[k].append(w)
        else:
            DC[k] = [w]
    while True:
        LETTERS, WORDLEN = input().split()
        if int(WORDLEN) == 0:
            break
        for spelled_word in get_words_from_letters(LETTERS, int(WORDLEN)):
            print(spelled_word)
        print('.')
