from sys import stdin
from itertools import repeat

def merge(decks):
    firsts = map(lambda e: e[0], decks)
    word = ''
    while decks:
        to_append = min(firsts)
        word += to_append[1]
        index = firsts.index(to_append)
        del decks[index][0]
        if decks[index]:
            firsts[index] = decks[index][0]
        else:
            del decks[index]
            del firsts[index]
    return word


decks = []
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    decks.append(deck)
print merge(decks)
