from sys import stdin

def sorter(A):
    # Merk: den sorterte lista ma returneres
    # A = [192, 291, 999, 1, 23]
    largest = len(str(max(A)))
    bucket = {i:[] for i in xrange(10)}
    for i in xrange(largest):
      for digit in A:
        try:
          cur_digit = int(str(digit)[-1-i], 10)
          bucket[cur_digit].append(digit)
        except IndexError:
          bucket[0].append(digit)
      A = []
      for n in bucket.keys():
        A += bucket[n]
        bucket[n] = []
    return A

def bs(A, t):
  minst = 0
  maks = len(A)-1
  while True:
    if maks < minst:
      return m
    m = (minst + maks) // 2
    if A[m] < t:
      minst = m + 1
    elif A[m] > t:
      maks = m - 1
    else:
      return m

def finn(A, nedre, ovre):
    # Merk: resultatet ma returneres
    n = bs(A, nedre)
    while n > 0 and A[n] > nedre:
      n -= 1
    o = bs(A, ovre)
    m = len(A)-1
    while o < m and A[o] < ovre:
      o += 1

    return [A[n], A[o]]

def main():
  liste = map(int, stdin.readline().split())
  sortert = sorter(liste)

  for linje in stdin:
      ord = linje.split()
      minst = int(ord[0], 10)
      maks = int(ord[1], 10)
      resultat = finn(sortert, minst, maks)
      print str(resultat[0]) + " " + str(resultat[1])

main()
