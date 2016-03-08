from sys import stdin

def avstand(s1, s2):
  len_s1 = len(s1)+1
  len_s2 = len(s2)+1
  matrix = [[0 for x in xrange(len_s1)] for y in xrange(len_s2)]
  matrix[0] = [x for x in xrange(len_s1)]
  for y in xrange(len_s2):
    matrix[y][0] = y
  for y in xrange(1,len_s2):
    for x in xrange(1,len_s1):
      if s2[y-1] == s1[x-1]:
        matrix[y][x] = matrix[y-1][x-1]
      else:
        matrix[y][x] = min(matrix[y-1][x]+1, matrix[y][x-1]+1, matrix[y-1][x-1]+1)
  return matrix[len_s2-1][len_s1-1]

def minste_avstand(strenger):
  # Return the minimal sum of distances from one string to another
  w = len(strenger)
  results = {n:0 for n in xrange(w)}
  for i in xrange(w):
    for n in xrange(i+1,w):
        weight = avstand(strenger[i], strenger[n])
        results[i] += weight
        results[n] += weight
  return min(results.values())

def main():
  linjer = map(lambda l: l.strip(), stdin.readlines())
  print minste_avstand(linjer)
main()
