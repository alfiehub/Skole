from sys import stdin

# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner

class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0

def dfs(rot):
    stakk = [rot]
    while True:
      l = stakk[-1]
      if l.ratatosk:
        return len(stakk)-1
      elif l.nesteBarn < len(l.barn):
        stakk.append(l.barn[l.nesteBarn])
        stakk[-2].nesteBarn += 1
      else:
        stakk.pop()

def bfs(rot):
    adj = [rot]
    adj_next = []
    c = 0
    while True:
        for v in adj:
            if v.ratatosk:
                return c
            else:
                for node in v.barn:
                    adj_next.append(node)
        adj = adj_next
        adj_next = []
        c += 1



funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print(dfs(start_node))
elif funksjon == 'bfs':
    print(bfs(start_node))
elif funksjon == 'velg':
    print(bfs(start_node))
