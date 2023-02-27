import tkinter
from PIL import Image, ImageTk

import os

_file_dir = os.path.dirname(os.path.realpath(__file__))

class Card(tkinter.Frame):
    """
    A card in the game.
    """
    
    NUMBERS = {0: "1", 1: "2", 2: "3"}
    COLORS = {0: "red", 1: "blue", 2: "gold"}
    FILLS = {0: "solid", 1: "open", 2: "striped"}
    SHAPES = {0: "oval", 1: "diamond", 2: "star"}

    WIDTH = 160
    HEIGHT = 100
    
    def __init__(self, master, number, color, fill, shape):
        self.master = master
        super().__init__(self.master)

        image_path = os.path.join(
            _file_dir,
            "images/cards/{}_{}_{}_{}.png".format(
                Card.NUMBERS[number],
                Card.COLORS[color],
                Card.FILLS[fill],
                Card.SHAPES[shape],
            )
        )
        
        self.image = Image.open(image_path)
        self.image = self.image.resize((Card.WIDTH, Card.HEIGHT), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.button = tkinter.Button(self, image=self.image, command=self.callback)
        self.button.pack()

        self.selected=False
        self.config(highlightthickness=5)
        self.config(highlightbackground="cyan", highlightcolor="blue")


    def callback(self):
        self.selected ^= True
        
        if self.selected:
            self.config(highlightbackground="red", highlightcolor="red2")
        else:
            self.config(highlightbackground="cyan", highlightcolor="blue")

        self.master.check_cards()

    def set_selected(self, value):
        self.selected = value
        
        if self.selected:
            self.config(highlightbackground="red", highlightcolor="red2")
        else:
            self.config(highlightbackground="cyan", highlightcolor="blue")

if __name__ == "__main__":
    root = tkinter.Tk()
    card = Card(root, 3, "blue", "striped", "star")
    card.pack()
    root.mainloop()
