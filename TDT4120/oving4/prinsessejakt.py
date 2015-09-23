# -*- coding: utf-8 -*-
from sys import *
import traceback

def subgraftetthet(nabomatrise, startnode):
    n = len(nabomatrise)
    # Min kode
    hovedgraf_noder = [startnode]
    utraversert = [startnode]
    rad = nabomatrise[startnode]

    while len(utraversert) > 0:
      cur_node = utraversert.pop()
      rad = nabomatrise[cur_node]
      for i in xrange(len(rad)):
        if rad[i] and i not in hovedgraf_noder:
          hovedgraf_noder.append(i)
          utraversert.append(i)

    noder_ikke_i_hovedgraf = [i for i in range(len(nabomatrise)) if i not in hovedgraf_noder]

    big_e = 0
    big_v = 0

    for startnode in noder_ikke_i_hovedgraf:
      e = 0
      v = 1
      cur_subgraf = [startnode]
      ikke_traversert = [startnode]
      while len(ikke_traversert) > 0:
        cur_node = ikke_traversert.pop()
        rad = nabomatrise[cur_node]
        for i in range(len(rad)):
          if i not in hovedgraf_noder and rad[i]:
            if i not in cur_subgraf:
              cur_subgraf.append(i)
              ikke_traversert.append(i)
              v += 1
              e += 1
            elif i in cur_subgraf:
              e += 1
      if float(e) > big_e:
        big_e = float(e)
        big_v = float(v)

      print(big_e,big_v)
      return big_e/big_v**2 if big_v != 0 else 0


try:
    n = int(stdin.readline())
    nabomatrise = [None] * n # rader
    for i in range(0, n):
        nabomatrise[i] = [False] * n # kolonner
        linje = stdin.readline()
        for j in range(0, n):
            nabomatrise[i][j] = (linje[j] == '1')
    for linje in stdin:
        start = int(linje)
        print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
except:
    traceback.print_exc(file=stderr)
