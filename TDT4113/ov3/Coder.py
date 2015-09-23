class Coder:
  def gen_message_from_file(self, filepath):
    f = open(filepath, 'r')
    return f.read().strip('\n').lower()

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
