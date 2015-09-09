class Action:
  def __init__(self, action):
    self.action = action

  def __eq__(self, other):
    return self.action == other

  def __gt__(self, other):
    if self.action != other:
      if self.action == 'paper':
        if other == 'scissor':
          return False
        elif other == 'rock':
          return True
      elif self.action == 'scissor':
        if other == 'rock':
          return False
        elif other == 'paper':
          return True
      elif self.action == 'rock':
        if other == 'scissor':
          return True
        elif other == 'paper':
          return False
    else:
      return False
