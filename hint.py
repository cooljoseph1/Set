import tkinter

class Hint(tkinter.Frame):
    """
    A hint button
    """
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)

        self.button = tkinter.Button(self, text="Hint", command=self.callback)
        self.button.pack()

    def callback(self):
        self.master.use_hint()
