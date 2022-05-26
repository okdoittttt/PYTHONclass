from tkinter import *

window = Tk()

b1 = Button(window, text="one", width=13)
b2 = Button(window, text="two")
b3 = Button(window, text="three", bd=5)

b1.grid(row=0, column=0)
b2.grid(row=1, column=1, padx=10, pady=5)
b3.grid(row=0, column=2, rowspan=2)

window.mainloop()