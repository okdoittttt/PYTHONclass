from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")
root.geometry("400x400+400+0")

def time():
    string = strftime('%H:%M:%S %P')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("DS-Digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')
time()

mainloop()