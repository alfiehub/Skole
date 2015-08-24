from singlegame import SingleGame
from manygames import ManyGames
from player import Player
from random_player import RandomPlayer
from seq_player import SeqPlayer
from most_common_player import MostCommonPlayer
from historian_player import HistorianPlayer

from gui import GUITournament

# Styrer spiller gjennom Tkinter/GUI.
root = Tk()
# Definer et vindu med gitte dimensjoner
root.geometry("1100x500+300+300")
# Lag instans, og kjoer oppsett av GUI (knapper etc)
GUITournament(root, Historiker(2)).setup_gui()
# Vis vindu, og utfoer tilhoerende kommandoer
root.mainloop()
