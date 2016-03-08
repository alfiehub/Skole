from sys import stdin

class Kubbe:
  vekt = None
  neste = None
  def __init__(self, vekt):
    self.vekt = vekt 
    self.neste = None 

def spor(kubbe):
  l = kubbe.vekt
  cur = kubbe
  # If you use cur.next here, the while loop will break before checking the last item
  while cur != None:
    l = cur.vekt if cur.vekt > l else l
    cur = cur.neste
  return l

# Oppretter lenket liste
forste = None
siste = None
for linje in stdin:
  forrige_siste = siste
  siste = Kubbe(int(linje))
  if forste == None:
    forste = siste
  else:
    forrige_siste.neste = siste

# Kaller loesningsfunksjonen og skriver ut resultatet
print(spor(forste))
