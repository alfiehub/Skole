from tkinter import Tk, BOTH, StringVar
from tkinter.ttk import Frame, Button, Label, Style
import pylab
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
from numpy import cumsum

from singlegame import SingleGame
from action import Action


class GUITournament(Frame):
  # Klassen GUITournament definerer en turnering mellom menneske
  # og en Spiller
  spiller = None

  # Resultater holder resultatet av kampene - for plotting
  resultater = None

  # Denne labelen vil brukes for aa rapportere enkeltspill
  resultat_label = None

  def __init__(self, parent, motspiller):
      Frame.__init__(self, parent)
      self.parent = parent

      # Huske hvem vi spiller mot
      self.spiller = motspiller

      # Initiere listen av resultater
      self.resultater = []

      # Foreloepig ikke noe aa rapportere
      self.resultat_label = StringVar()
      self.resultat_label.set("Du spiller mot %s" % self.spiller.get_name())
      self.style = Style()
      self.fig = None

  def setup_gui(self):
      self.parent.title("Stein - Saks - Papir")
      self.style.theme_use("default")
      self.pack(fill=BOTH, expand=1)

      # Label for rapportering
      label = Label(self.parent, textvariable=self.resultat_label)
      label.place(x=800, y=50)

      # Buttons
      # Disse fyrer av metoden self.arranger_enkeltspill som er
      # definert i klassen. Denne metoden tar aksjonen til mennesket
      # som startup, og gjennomfoerer spillet
      # Samme type oppfoersel for de tre aksjons-knappene
      rock_button = Button(self, text="Stein",
      command=lambda: self.arranger_enkeltspill(Action("rock")))
      rock_button.place(x=800, y=400)
      scissors_button = Button(self, text="Saks",
      command=lambda: self.arranger_enkeltspill(Action("scissor")))
      scissors_button.place(x=900, y=400)
      paper_button = Button(self, text="Papir",
      command=lambda: self.arranger_enkeltspill(Action("paper")))
      paper_button.place(x=1000, y=400)

      # quit_button avslutter GUI'et naar den trykkes
      quit_button = Button(self, text="Quit", command=self.quit)
      quit_button.place(x=1000, y=450)
      # Embedde en graf i vinduet for aa rapportere fortloepende score
      self.fig = FigureCanvasTkAgg(pylab.figure(), master=self)
      self.fig.get_tk_widget().grid(column=0, row=0)
      self.fig.show()


  def arranger_enkeltspill(self, handling):
    player1_action = self.spiller.choose_action()
    player2_action = handling
    self.p1_action = player1_action.action
    self.p2_action = handling

    self.resultat = self.resultater

    if player1_action == player2_action:
      self.spiller.get_result(player2_action, 0.5)
      self.resultat.append(0.5)
    elif player1_action > player2_action:
      self.spiller.get_result(player2_action, 1)
      self.resultat.append(0)
    else:
      self.spiller.get_result(player2_action, 0)
      self.resultat.append(1)

    # Update plot
    plt.figure(self.fig.figure.number)  # Handle til figuren
    plt.ion()
    plt.plot(range(1, len(self.resultat) + 1),
    100 * cumsum(self.resultat) /
    range(1, len(self.resultat) + 1), 'b-', lw=4)
    plt.ylim([0, 100])
    plt.xlim([1, max(1.1, len(self.resultat))])
    plt.plot(plt.xlim(), [50, 50], 'k--', lw=2)
    plt.grid(b=True, which='both', color='0.65', linestyle='-')
    self.fig.show()
