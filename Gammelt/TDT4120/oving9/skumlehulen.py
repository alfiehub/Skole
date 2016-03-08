from sys import stdin, stderr

# kapasiteter er den opprinnelige kapasitetsmatrisen, som inneholder n x n elementer (hvor n er antall noder).
# startrom er en liste med indeksene til nodene som tilsvarer startrommene.
# utganger er en liste med indeksene til nodene som tilsvarer utgangene.

def antallIsolerteStier(kapasiteter, startrom, utganger):
  # First you have to expand the capacity matrix
  # Basically transform it from and adjacency matrix to an edge matrix
  """
  1 1 1
  1 0 1
  1 1 1
  ===
  (i,j) and (j,i) is the same edge - edge(i,j) == -edge(j,i)
  We only have to add the super-source and sink once, because we can add their edge by only adding them
  """
  # Split all nodes, add super sink and super source
  n = len(kapasiteter)
  m = len(kapasiteter) * 2 + 2
  C = [[0 for x in xrange(m)] for y in xrange(m)]
  for node in startrom:
    C[0][node*2+1] = 1 # Fill inn all the edges from the super-source to the sources
  for y in xrange(n):
    for x in xrange(n):
      # C[y][x] - weight of the edge going out of y and into x
      # Therefore this can be viewed as an edge from y_2 to x_1
      C[y*2+2][x*2+1] = kapasiteter[y][x]
  for i in xrange(n): # Connect all the splitted nodes to each other
    C[i*2+1][i*2+2] = 1
  for node in utganger: # Fill all the sinks
    C[node*2+2][-1] = 1 # All outgoing nodes is going from node_2 to the last noe _1
    # All outgoing edges goes from _2 for each node.
  # C should now be complete

  F = [[0 for x in xrange(m)] for y in xrange(m)]
  c = 0
  while True:
    path = finnFlytsti(0, m-1, F, C)
    if not path:
      return c
    for z in xrange(len(path)-1):
      # The edge from z -> z+1 is incremented by one
      # The inverse edge (same edge, just the reveresed direction) gets decremented
      F[path[z]][path[z+1]] += 1
      F[path[z+1]][path[z]] -= 1
    c += 1
    if c == len(startrom):
      return c


def finnFlytsti(kilde, sluk, F, C):
    n = len(F)
    oppdaget = [False] * n
    forelder = [None] * len(F)
    koe = [kilde]
    while koe:
        node = koe.pop(0)
        if node == sluk:
            # Har funnet sluken, lager en array med passerte noder
            sti = []
            i = node
            while True:
                sti.append(i)
                if i == kilde:
                    break
                i = forelder[i]
            sti.reverse()
            return sti;
        for nabo in range(n):
            if not oppdaget[nabo] and F[node][nabo] < C[node][nabo]:
                koe.append(nabo);
                oppdaget[nabo] = True;
                forelder[nabo] = node;
    return None

noder, _, _ = [int(x) for x in stdin.readline().split()]
startrom = [int(x) for x in stdin.readline().split()]
utganger = [int(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [int(nabo) for nabo in linje.split()]
    nabomatrise.append(naborad)
print antallIsolerteStier(nabomatrise, startrom, utganger)
