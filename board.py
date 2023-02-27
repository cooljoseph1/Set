import tkinter

from game import Game
from card import Card

class Board(tkinter.Frame):
    """
    Frame that includes all of the cards
    """
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)
        
        self.cards = [Card(self, *card) for card in self.master.game.cards_in_play]

        for y in range(0, len(self.cards), 3):
            for x in range(3):
                self.cards[y + x].grid(row=y, column=x)

    def check_cards(self):
        selected_cards = [i for i, card in enumerate(self.cards) if card.selected]

        if len(selected_cards) != 3:
            return

        self.master.game.make_move(*selected_cards)
        
        old_cards = self.cards
        self.cards = [Card(self, *card) for card in self.master.game.cards_in_play]

        for y in range(0, len(self.cards), 3):
            for x in range(3):
                self.cards[y + x].grid(row=y, column=x)

        for card in old_cards:
            card.destroy()
