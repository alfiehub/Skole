from singlegame import SingleGame
from manygames import ManyGames
from player import Player
from random_player import RandomPlayer
from seq_player import SeqPlayer
from most_common_player import MostCommonPlayer
from historian_player import HistorianPlayer
from manygames_gui import ManyGames_GUI


from gui import GUITournament
from tkinter import Tk, BOTH, StringVar

## Styrer spiller gjennom Tkinter/GUI.
#root = Tk()
## Definer et vindu med gitte dimensjoner
#root.geometry("1100x500+300+300")
## Lag instans, og kjoer oppsett av GUI (knapper etc)
#GUITournament(root, HistorianPlayer(3)).setup_gui()
## Vis vindu, og utfoer tilhoerende kommandoer
#root.mainloop()

play = ManyGames_GUI(HistorianPlayer(2), HistorianPlayer(3), 2000)
play.play_tournament()
