from ASCII import ASCII
from Huffcoder import Huffcoder
import PythonLabs.BitLab as btl
from lz import lz

def ASCII_test(msg='Hello world', filepath=False,lz_flag=False):
  a = ASCII()
  if filepath != False:
    msg = a.gen_message_from_file(filepath)

  if lz_flag:
    l = lz()
    a.encode_decode_test(msg)
    ascii_encode = a.encode(msg)
    print('Encode, decode test with LZ. After Huff encoding')
    l.encode_decode_test(ascii_encode)

  else:
    a.encode_decode_test(msg)

def Huff_test(msg='Hello World',filepath=False,lz_flag=False):
  h = Huffcoder()
  if filepath != False:
    msg = h.gen_message_from_file(filepath).replace('\n', '')

  if lz_flag:
    l = lz()
    h.encode_decode_test(msg)
    print('Encode, decode test with LZ. After Huff encoding')
    huff_encoded = h.encode(msg)
    l.encode_decode_test(huff_encoded.__repr__())

  else:
    h.encode_decode_test(msg)

def LZ_test(msg='000000000000000000000',filepath=False):
  l = lz()
  if filepath != False:
    msg = l.gen_message_from_file(filepath)

  l.encode_decode_test(msg)

LZ_test(filepath='./potus_bit.txt')
