import tkinter

class Timer(tkinter.Frame):
    """
    A timer.
    """
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)

        self.label = tkinter.Label(self, text="00:00")
        self.label.pack()
        self.seconds = -1
        self.minutes = 0
        self.update_clock()

    def update_clock(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        time_string = "{:02d}:{:02d}".format(self.minutes, self.seconds)
        self.label.configure(text=time_string)
        self.after(1000, self.update_clock)
