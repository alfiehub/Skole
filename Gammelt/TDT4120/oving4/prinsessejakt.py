# -*- coding: utf-8 -*-
from sys import stdin

def main():
    n = int(stdin.readline())
    nabomatrise = [None for i in xrange(n)]
    for i in xrange(n):
        nabomatrise[i] = [False] * n
        linje = stdin.readline()
        for j in xrange(n):
            nabomatrise[i][j] = (linje[j] == '1')
    for linje in stdin:
        start = int(linje)

        h_n = {start}
        utraversert = [start]

        while utraversert:
            rad = nabomatrise[utraversert.pop()]
            for i in xrange(n):
                if rad[i] and i not in h_n:
                    h_n.add(i)
                    utraversert.append(i)

        nrn = {i for i in xrange(n)} - h_n

        e = 0
        for node in nrn:
            row = nabomatrise[node]
            for i in xrange(n):
                if row[i] and i in nrn:
                    e += 1
        v = float(len(nrn))
        print "%.3f" % ((e / v**2 if v != 0 else 0) + 1E-12)

main()
