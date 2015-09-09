from singlegame import SingleGame

class ManyGames:
  def __init__(self, p1, p2, amount):
    self.p1 = p1
    self.p2 = p2
    self.amount = amount

  def __play_singlegame(self):
    game = SingleGame(self.p1, self.p2)
    print(game)

  def __win_percent(self, p):
    return (p.score/self.amount)*100

  def play_tournament(self):
    for n in range(0, self.amount):
      self.__play_singlegame()
    print('%s won %r%% \t %s won %r%%' % (self.p1.get_name(), self.__win_percent(self.p1), self.p2.get_name(), self.__win_percent(self.p2)))

