class SingleGame:
  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    self.__play_game()

  def __play_game(self):
    player1_action = self.player1.choose_action()
    player2_action = self.player2.choose_action()
    self.p1_action = player1_action.action
    self.p2_action = player2_action.action


    if player1_action == player2_action:
      self.player1.get_result(player2_action, 0.5)
      self.player2.get_result(player1_action, 0.5)
      self.winner = 'None wins'
    elif player1_action > player2_action:
      self.player1.get_result(player2_action, 1)
      self.player2.get_result(player1_action, 0)
      self.winner = self.player1.get_name() + 'wins'
    else:
      self.player1.get_result(player2_action, 0)
      self.player2.get_result(player1_action, 1)
      self.winner = self.player2.get_name() + 'wins'


  def __str__(self):
    return '%s played %s \t %s played %s \t\t %s' % (self.player1.get_name(), self.p1_action, self.player2.get_name(), self.p2_action, self.winner)
