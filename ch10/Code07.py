from tkinter import *
from math import *

def cal(event):
    label.configure(text="결과 : " + str(eval(entry.get())))
    entry.delete(0, END)

root = Tk()

Label(root, text="수식 입력 : ").pack()
entry = Entry(root)
entry.bind("<Return>", cal)
entry.pack()

label = Label(root, text="결과 : ")
label.pack()

root.mainloop()
