from tkinter import *
from tkinter import messagebox

# def myFunc():


window = Tk();

window.geometry("400x400+0+0")

photo = PhotoImage(file="img/dog1.jpg")
# btn1 = Button(window, image=photo, command=myFunc)

photo2 = PhotoImage(file="img/dog2.jpeg")
btn2 = Button(window, image=photo2, command=window.destroy())

# btn1.pack(side=LEFT)
btn2.pack()