# -*- coding: UTF-8 -*-

from sys import stdin

Inf = float(1e3000)
False = 0
True = 1

def mst_(nm):
    n = len(nm)
    mst = set([0])
    edges = set([])

    while len(mst) < n:
      not_visited = set(xrange(n)) - mst
      ce = Inf
      for node in mst:
        ces = [(nm[node][i], i) for i in not_visited] # Edges to nodes not yet in mst
        cce = min(ces)
        if cce[0] < ce:
          ce = cce[0]
          cn = cce[1]
      if ce != Inf:
        edges.add(ce)
        mst.add(cn)
    return max(edges)


# Alternativ mÃ¥te Ã¥ lage nabomatrise pÃ¥, fungerer ikke. print(nabomatrise) gir samme input
# Gir 0/5 pÃ¥ korrekthetstester og 0/50 pÃ¥ korrekthetspoeng
# WTF is this shit? Det burde jo gÃ¥ fint nÃ¥r begge produserer samme resultat.
#
# linjer = [map(lambda spl: (int(spl[0]), int(spl[2])), s.split()) for s in stdin.read().split('\n')]
# linjer.pop()
# indekser = [map(lambda e: e[0], li) for li in linjer]
# n = len(linjer)
# nabomatrise = [[linjer[y][indekser[y].index(x)][1] if x in indekser[y] else Inf for x in xrange(n)] for y in xrange(n)]
#
# print(nabomatrise) = [[inf, 5, 3, 7], [5, inf, inf, 1], [3, inf, inf, inf], [7, 1, inf, inf]]

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
# print(nabomatrise) = [[inf, 5, 3, 7], [5, inf, inf, 1], [3, inf, inf, inf], [7, 1, inf, inf]]
print mst_(nabomatrise)
