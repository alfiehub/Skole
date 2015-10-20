from sys import stdin, stderr
def beste_sti(nm, sans):
  n = len(nm)

  previous = [0] * n
  cumprob = [0.0] * n # Each node starts as unlikely

  cumprob[0] = sans[0]

  # For each iteration, select the node with highest probability as the current node, if this node hasnt been visited
  # You also need to specify the previous node for each you visit, so you can know what way youre going
  unvisited = set(xrange(n))

  while unvisited:
    if n-1 in unvisited:
      to_check = map(lambda e: (cumprob[e], e), unvisited)
      if not to_check:
        return '0'
      cur = max(to_check) # Select the best node
      unvisited.remove(cur[1]) # Remove it from unvisited, ie mark it as visited
      for nabo, val in enumerate(nm[cur[1]]):
        if val and nabo in unvisited:
          tilbud = cumprob[cur[1]] * sans[nabo]
          if tilbud > cumprob[nabo]:
            cumprob[nabo] = tilbud
            previous[nabo] = cur[1]
    else:
      break # If visited the last node, break


  if(cumprob[-1] == 0.0):
      return '0'
  index = n - 1
  sti = []
  while index != 0:
      sti.append(index)
      index = previous[index]
  sti.append(0)
  return '-'.join(map(str, reversed(sti)))



n = int(stdin.readline())
sannsynligheter = [float(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [0] * n
    naboer = [int(nabo) for nabo in linje.split()]
    for nabo in naboer:
        naborad[nabo] = 1
    nabomatrise.append(naborad)
print beste_sti(nabomatrise, sannsynligheter)
