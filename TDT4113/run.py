from singlegame import SingleGame
from manygames import ManyGames
from player import Player
from random_player import RandomPlayer
from seq_player import SeqPlayer
from most_common_player import MostCommonPlayer
from historian_player import HistorianPlayer

p1 = HistorianPlayer(2)
p2 = HistorianPlayer(3)

tournament = ManyGames(p1, p2, 1000)
tournament.play_tournament()
