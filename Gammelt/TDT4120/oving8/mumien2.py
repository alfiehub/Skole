from sys import stdin, stderr

def beste_sti(nm, sans):
    # START IKKE-UTDELT KODE
    n = len(sans)
    ferdig = [False] * n
    ksans = [0.0] * n # kummulativ sannsynlighet
    ksans[0] = sans[0]
    forrige = range(n)
    beste_node = 0
    for i in range(n):
        print(str(i) + '.')
        print(forrige)
        print(beste_node)
        print(ksans)
        node = beste_node # Currenet node == beste_node
        ferdig[node] = True # mark current node as visited/processed
        hoyeste_ksans = -1.0 # biggest ksans this iteration
        for nabo in range(n): # each neighbour
            if not ferdig[nabo]: # if not visited yet
                if nm[node][nabo]: # if there is a connection between the neighbour and current node
                    tilbud = ksans[node] * sans[nabo] # this is the probability if we visit this neighbour
                    if tilbud > ksans[nabo]: # if this is higher than what we already have for visiting that neighbour
                        forrige[nabo] = node # previous node for that neighbour is now the node
                        ksans[nabo] = tilbud # the probability when visiting that neighbour
                if ksans[nabo] > hoyeste_ksans: # if this neighbours prob is higher than any before, select this at the neighbour we want to visit
                    beste_node = nabo # set the next current node
                    hoyeste_ksans = ksans[nabo] # set the probability we have when visiting that node
    if(ksans[-1] == 0.0):
        return '0'
    index = n - 1
    sti = []
    while index != 0:
        sti.append(index)
        index = forrige[index]
    sti.append(0)
    return '-'.join(map(str, reversed(sti)))
    # SLUTT IKKE-UTDELT KODE

n = int(stdin.readline())
sansynligheter = [float(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [0] * n
    naboer = [int(nabo) for nabo in linje.split()]
    for nabo in naboer:
        naborad[nabo] = 1
    nabomatrise.append(naborad)
print beste_sti(nabomatrise, sansynligheter)
