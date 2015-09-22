from Coder import Coder
import PythonLabs.BitLab as btl
import kdprims

class Huffcoder(Coder):
  def __init__(self):
    filepath = './corpus1.txt'
    freqs = kdprims.calc_char_freqs(filepath)
    self.__build_tree(freqs)

  def __build_tree(self, freqs):
    pq = btl.init_queue(freqs)
    while len(pq) > 1:
      n1 = pq.pop()
      n2 = pq.pop()

      pq.insert(btl.Node(n1,n2))
    self.tree = pq[0]

  def encode(self, msg):
    return btl.huffman_encode(msg, self.tree)


  def decode(self, encoded):
    return btl.huffman_decode(encoded, self.tree)
