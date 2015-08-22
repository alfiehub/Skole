from singlegame import SingleGame
from player import Player
from random_player import RandomPlayer

p1 = Player()
p2 = RandomPlayer()

game = SingleGame(p1,p2)
print(p2.get_name())
print(game)
