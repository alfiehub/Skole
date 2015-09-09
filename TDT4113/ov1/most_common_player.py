from player import Player
from action import Action
from action import Action
from random import randint

class MostCommonPlayer(Player):
  def __init__(self):
    self.score = 0
    self.rock_count = 0
    self.paper_count = 0
    self.scissor_count = 0

  def get_result(self, other, result):
    o = other.action
    if o == 'rock':
      self.rock_count += 1
    elif o == 'paper':
      self.paper_count += 1
    else:
      self.scissor_count += 1

    self.score += result

  def choose_action(self):
    counters = [self.rock_count, self.paper_count, self.scissor_count]
    i = counters.index(max(counters))

    options = ['rock', 'paper', 'scissor']
    return Action(options[i])
