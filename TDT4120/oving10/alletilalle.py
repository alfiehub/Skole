from sys import stdin, maxint

def korteste_rute(rekkefolge, V, byer):
    # Floyd-Warshall - alle til alle
    for k in xrange(byer):
      for i in xrange(byer):
        for j in xrange(byer):
          alt = V[i][k] + V[k][j]
          if V[i][j] > alt:
            V[i][j] = alt

    w = 0
    for i in xrange(len(rekkefolge)-1):
      w += V[rekkefolge[i]][rekkefolge[i+1]]

    # Connect the last node the first one in the rekkefolge. This assumes that this shortest path goes through all the previous cities in the rekkefolge.
    # Its basically assuming that the shortest path we took from the start node to the last node is the same as the shortest path from the last one to the first
    w += V[rekkefolge[-1]][rekkefolge[0]]

    return w if w < maxint else 'umulig'



testcases = int(stdin.readline())
for test in range(testcases):
    byer = int(stdin.readline())
    rekkefolge = map(int, stdin.readline().split())
    nabomatrise = []
    for by in xrange(byer):
      nabomatrise.append(map(lambda i: int(i, 10) if i != '-1' else maxint, stdin.readline().split()))
    print korteste_rute(rekkefolge, nabomatrise, byer)
