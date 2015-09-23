from Coder import Coder

class ASCII(Coder):
  def __to_8bit(self, char):
    numb = int(char)
    b = bin(numb)[2:]
    # Add the the missing zeroes to make it 8 bit and return it
    return '0'*(8-len(b)) + b

  def __from_8bit(self, bits):
    # Convert string bits to an integer with base 2
    return int(bits, 2)

  def encode(self, string):
    encoded = ''
    for c in string:
      encoded += self.__to_8bit(str(ord(c)))
    return encoded

  def decode(self, bits):
    decoded = ''
    for i in range(0, len(bits), 8):
      decoded += str(chr(self.__from_8bit(bits[i:i+8])))
    return decoded

  def encode_decode_test(self, message):
    encoded = self.encode(message)
    decoded = self.decode(encoded)

    print(self.__class__.__name__)
    print('Message == decoded' if message == decoded else "Message != decoded")
    print(message)
    print(encoded)
    print(decoded)

    print("M: %d \t E: %d \t D: %d" % (len(message), len(encoded), len(decoded)))

    print('Compression fraction: %r' % (1-(len(encoded)/(len(message)))))
    print('-'*50)
