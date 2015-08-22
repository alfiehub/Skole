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
      self.winner = 'it even :('
    elif player1_action > player2_action:
      self.player1.get_result(player2_action, 1)
      self.player2.get_result(player1_action, 0)
      self.winner = 'player 1 win'
    else:
      self.player1.get_result(player2_action, 0)
      self.player2.get_result(player1_action, 1)
      self.winner = 'player 2 win'


  def __str__(self):
    return 'Player1 played %s and player2 played %s, which makes %s' % (self.p1_action, self.p2_action, self.winner)
