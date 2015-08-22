from action import Action

class Player:
  def __init__(self):
    print('Intializing player')
    self.score = 0

  def choose_action(self):
    action = str(input('Rock, paper or scissor? ')).lower()
    if action not in ['rock', 'paper', 'scissor']:
      print('That is not a valid option!')
      return self.choose_action()
    else:
      return Action(action)

  def get_result(self, other_action, result):
    self.score += result

  def get_name(self):
    return self.__class__.__name__
