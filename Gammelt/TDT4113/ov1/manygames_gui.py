from singlegame import SingleGame
import numpy as np
import matplotlib.pyplot as plt

class ManyGames_GUI:
  def __init__(self, p1, p2, amount):
    self.p1 = p1
    self.p2 = p2
    self.amount = amount
    self.y = []

  def __play_singlegame(self):
    game = SingleGame(self.p1, self.p2)

  def __win_percent(self, p):
    return (p.score/self.amount)*100


  def play_tournament(self):
    plt.axis([0,self.amount, 0, 1])
    plt.ion()
    plt.hlines(y=0.5, xmin=0, xmax=self.amount, linestyles='dotted')
    plt.title('%s sin vinnerprosent vs %s' % (self.p1.get_name(), self.p2.get_name()))
    plt.show()
    for n in range(0, self.amount):
      self.__play_singlegame()
      x = np.arange(0,n+1,1)
      self.y.append(self.p1.score/(n+1))
      plt.plot(x,self.y, c='b')
      plt.axis([0,n+1, 0, 1])
      plt.draw()
    print('%s won %r%% \t %s won %r%%' % (self.p1.get_name(), self.__win_percent(self.p1), self.p2.get_name(), self.__win_percent(self.p2)))

