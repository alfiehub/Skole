from sys import stdin, maxint
from heapq import heappop, heappush

def korteste_rute(rekkefolge, nabomatrise, n):
    w = 0
    for i in xrange(n):
        start = rekkefolge[i]
        slutt = rekkefolge[(i+1)%n] # This modulo only triggers the last iteration, making i == n-1 and (i+1)%n == 0. Basically the last element of rekkefolge and the first
        dist = {x:maxint for x in xrange(n)}
        dist[start] = 0
        heap = [(0, start)]
        while True:
          u = heappop(heap)[1]
          if u == slutt:
            break
          for nabo, val in enumerate(nabomatrise[u]):
            if val < maxint:
              alt = dist[u] + val
              if alt < dist[nabo]:
                dist[nabo] = alt
                heappush(heap, (alt, nabo)) # Push and fix stuff
          if not heap:
            break
        w += dist[slutt]
    return w if w < maxint else 'umulig'

def main():
    testcases = int(stdin.readline(), 10)
    for test in range(testcases):
        byer = int(stdin.readline(), 10)
        rekkefolge = map(int, stdin.readline().split())
        nabomatrise = []
        for by in range(byer):
            nabomatrise.append(map(lambda i: int(i,10) if i != '-1' else maxint, stdin.readline().split()))
        print korteste_rute(rekkefolge, nabomatrise, byer)
main()
