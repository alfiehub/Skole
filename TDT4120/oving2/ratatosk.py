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

#def dfs(rot):
#    # SKRIV DIN KODE HER

def bfs(rot):
    adj = rot.barn
    adj_next = []
    cur_level = 0
    c = 0
    while True:
        c += 1
        for v in adj:
            if v.ratatosk:
                return c
            else:
                for node in v.barn:
                    adj_next.append(node)
        adj = adj_next
        adj_next = []



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
