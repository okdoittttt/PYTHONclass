from tkinter import *

def show():
    print("이름 : %s \n 나이 : %s"%(e1.get(), e2.get()))
    e1.insert(END, 3.5)

root = Tk()
root.geometry("300x150")

Label(root, text="이름").place(x=20, y=20)
Label(root, text="나이").place(x=20, y=50)

e1 = Entry(root)
e2 = Entry(root, show="*")

e1.place(x=60, y=20)
e2.place(x=60, y=50)

Button(root, text="보이기", command=show).place(x=70, y=80)
Button(root, text="종료", command=quit).place(x=170, y=80)

root.mainloop()