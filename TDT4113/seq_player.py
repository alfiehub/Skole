from player import Player
from action import Action
from action import Action
from random import randint

class SeqPlayer(Player):
  def __init__(self):
    self.score = 0
    self.c = 0
  def choose_action(self):
    self.c = (self.c+1) % 3

    options = ['rock', 'paper', 'scissor']
    return Action(options[self.c])
