from tkinter import *

window = Tk()

window.geometry("400x400+0+0")

def clicked():
    print("Clicked Button!")

btn = Button(window, text='Button', command=clicked)
btn.pack()

window.mainloop()