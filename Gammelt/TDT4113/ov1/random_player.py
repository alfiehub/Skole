from player import Player
from action import Action
from action import Action
from random import randint

class RandomPlayer(Player):
  def choose_action(self):
    options = ['rock', 'paper', 'scissor']
    return Action(options[randint(0,2)])
