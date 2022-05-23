from tkinter import *

window = Tk()

window.title("Window Test")
window.geometry("400x400+100+0")
window.resizable(True, False)

label1 = Label(window, text='A')
label2 = Label(window, text='B')
label3 = Label(window, text='C', anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
