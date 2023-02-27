#!/usr/bin/env python3

import tkinter
from window import Window

def main():
    root = tkinter.Tk()
    root.title("Set")
    window = Window(root)
    window.pack(fill=tkinter.BOTH, expand=1)
    root.mainloop()

if __name__ == "__main__":
    main()
