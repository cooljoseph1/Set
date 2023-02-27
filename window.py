import tkinter

from game import Game
from board import Board
from hint import Hint
from timer import Timer

class Window(tkinter.Frame):
    """
    Main frame for the game
    """
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)

        self.game = Game()
        self.board = Board(self)
        

        self.hint = Hint(self)
        self.timer = Timer(self)
        
        self.timer.grid(row=0, column=0)
        self.hint.grid(row=0, column=2)

        self.board.grid(row=1, column=0, columnspan=3, sticky=tkinter.NSEW)
        
    def use_hint(self):
        for card in self.board.cards:
            card.set_selected(False)

        hints = self.game.hint()
        if hints is not None:
            for hint in hints:
                self.board.cards[hint].config(highlightbackground="yellow", highlightcolor="gold")
