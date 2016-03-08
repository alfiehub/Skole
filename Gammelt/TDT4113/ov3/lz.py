from Coder import Coder
import math

class lz(Coder):
  def __integer_to_bits(self, integer, bitlen):
    b = bin(integer)[2:]
    return '0'*(bitlen-len(b)) + b

  def __bits_to_integer(self, string):
    return int(string, 2)

  def find_next_segment(self, source, loc, lt):
    seg = oldseg = ''
    newbit = ''

    while lt.get(seg,-1) >= 0:
      if loc >= len(source):
        return [seg, '']
      newbit = source[loc]
      loc += 1
      oldseg = seg
      seg += newbit
    return [oldseg, newbit]

  def encode(self, source):
    # Source is a string
    slen = len(source)
    target = source[0]
    lt = {'' : 0, source[0] : 1}
    size = 2
    currloc = 1
    while currloc < slen:
      oldseg, newbit = self.find_next_segment(source, currloc, lt)
      bitlen = math.ceil(math.log(size, 2))
      index = lt[oldseg]
      index_bits = self.__integer_to_bits(index, bitlen)

      target += index_bits + newbit
      lt[oldseg+newbit] = len(lt.keys())
      currloc += len(oldseg) + 1
      size += 1
    return target

  def decode(self, target):
    tlen = len(target)
    source = target[0]
    lt = ['', target[0]]
    loc = 1
    size = 2

    while loc < tlen:
      bitlen = math.ceil(math.log(size, 2))
      index = int(target[loc : loc+bitlen], 2)
      seg = lt[index]

      if loc + bitlen < tlen:
        seg += target[loc+bitlen]
        size += 1
        lt.append(seg)
        loc += 1
      source += seg
      loc += bitlen
    return source


