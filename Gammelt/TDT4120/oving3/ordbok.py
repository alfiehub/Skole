from sys import stdin, stderr
import traceback

class Node:
  def __init__(self):
    self.barn = {}
    self.posi = []

def bygg(ordliste):
  toppnode = Node()
  for entry in ordliste:
    word = entry[0]
    tmp_node = toppnode
    for i in word:
      # Hvis ikke noden finnes, lag en
      if not i in tmp_node.barn:
        tmp_node.barn[i] = Node()
      tmp_node = tmp_node.barn[i]
      # Hvis ordet er ferdig, legg til indexen
      if i == word[-1]:
        tmp_node.posi.append(entry[1])
  return toppnode

def posisjoner(ord, indeks, node):
  if indeks < len(ord):
    if ord[indeks] in node.barn:
      return posisjoner(ord, indeks+1, node.barn[ord[indeks]])
    elif ord[indeks] == '?':
      pos = []
      for key in node.barn:
        pos.extend(posisjoner(ord, indeks+1, node.barn[key]))
      return pos
    else:
      return []
  elif len(ord) == indeks:
    return node.posi
  else:
    return []

def main():
  try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
      ordliste.append( (o,pos) )
      pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
      sokeord = sokeord.strip()
      print sokeord + ":",
      posi = sorted(posisjoner(sokeord, 0, toppnode))
      for p in posi:
        print p,
      print
  except:
    traceback.print_exc(file=stderr)
main()
