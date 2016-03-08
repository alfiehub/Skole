from sys import stdin, stderr

def siftUp(A, vals, node):
  child = node
  while child > 0:
    root = (child-1)//2
    if vals[A[child]] > vals[A[root]]:
      A[root], A[child] = A[child], A[root]
      child = root
    else:
      return
def siftDown(A, vals, node):
  root = node
  end = len(A)-1
  while root * 2 + 1 < end:
    child = root * 2 + 1
    if child + 1 <= end and vals[A[child]] < vals[A[child+1]]:
      child += 1
    if vals[A[root]] < vals[A[child]]:
      A[root], A[child] = A[child], A[root]
      root = child
    else:
      return

def beste_sti(nm, sans):
  n = len(nm)
  prev = {i:0 for i in xrange(n)}
  cumsans = {i:0.0 for i in xrange(n)}
  cumsans[0] = sans[0]
  pri_q = range(n)
  while True:
    if pri_q:
      u = pri_q[0]
      pri_q[0] = pri_q[-1]
      del pri_q[-1]
      siftDown(pri_q, cumsans, 0)

      for v in pri_q:
        if nm[u][v]:
          alt = cumsans[u] * sans[v]
          if alt > cumsans[v]:
            prev[v] = u
            if v == n-1: # The first time we encounter the last node, we know that we have found the optimal path to it
              return returnOutput(prev, n-1)
            cumsans[v] = alt
            siftUp(pri_q, cumsans, pri_q.index(v))
    else:
      return '0'
  return returnOutput(prev, n-1)


def returnOutput(prev, index):
  p = []
  while index != 0:
    p.append(index)
    index = prev[index]
  p.append('0')
  return reduce(lambda a,b: a+'-'+b, map(str, p[::-1]))

def main():
  n = int(stdin.readline())
  sannsynligheter = {n:float(val) for n, val in enumerate(stdin.readline().split())}
  nabomatrise = []
  for linje in stdin:
      naborad = [0] * n
      naboer = map(int, linje.split())
      for nabo in naboer:
          naborad[nabo] = 1
      nabomatrise.append(naborad)
  print beste_sti(nabomatrise, sannsynligheter)
main()
