# -*- coding: UTF-8 -*-

from sys import stdin
from random import randint

Inf = float(1e3000)
False = 0
True = 1

def mst_(nm):
    n = len(nm)
    mst = set([1])
    edges = set()

    while len(mst) < n:
        not_in = set(xrange(n)) - mst
        this_round = set()
        for target in not_in:
            target_row = [(nm[target][origin], target) for origin in mst]
            this_round.add(min(target_row))
        # (weight, target)
        edges.add(min(this_round)[0])
        mst.add(min(this_round)[1])

    return max(edges)

linjer = []
for str in stdin:
    linjer.append(str)
n = len(linjer)
nabomatrise = [None] * n
node = 0
for linje in linjer:
    nabomatrise[node] = [Inf] * n
    for k in linje.split():
        data = k.split(':')
        nabo = int(data[0])
        vekt = int(data[1])
        nabomatrise[node][nabo] = vekt
    node += 1
print mst_(nabomatrise)
