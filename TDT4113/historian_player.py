from player import Player
from action import Action
from action import Action
from random import randint

class HistorianPlayer(Player):
  def __init__(self, remember):
    self.score = 0
    self.history = []
    self.remember = remember

  def get_result(self, other, result):
    self.history.append(other)

    self.score += result

  def choose_action(self):
    rock_count = 0
    paper_count = 0
    scissor_count = 0
    options = ['rock', 'paper', 'scissor']
    actions = [Action('rock'), Action('paper'), Action('scissor')]

    if len(self.history) > self.remember:
      last = self.history[-self.remember:]
      last_actions = list(map(lambda a: a.action, last))

      i = len(self.history)
      for n in range(i-self.remember, 0, -1):
        last_enemy = self.history[n-self.remember:n]
        last_enemy_actions = list(map(lambda a: a.action, last_enemy))

        if last_actions == last_enemy_actions:
          o = self.history[n].action
          if o == 'rock':
            rock_count += 1
          elif o == 'paper':
            paper_count += 1
          else:
            scissor_count += 1


        counters = [rock_count, paper_count, scissor_count]

        most_likely = Action(options[counters.index(max(counters))])
        my_next_action = list(filter(lambda a: a > most_likely, actions))

        return my_next_action[0]
    else:
      return actions[randint(0,2)]

  def get_name(self):
    return self.__class__.__name__ + '(' + str(self.remember) + ')'
