from tkinter import *

win = Tk()
win.geometry("300x300")

b1 = Button(win, text='one')
b2 = Button(win, text='two')
b3 = Button(win, text='three')
b4 = Button(win, text='four')

b1.grid(row=0, column=0, rowspan=2)
b2.grid(row=0, column=1)
b3.grid(row=1, column=1)
b4.grid(row=2, column=0, columnspan=2)

win.mainloop()
