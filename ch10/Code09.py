from tkinter import *
def show() :
    print ("이름 : %s \n비밀번호 : %s" % (e1.get(), e2.get()))
    e1.delete(0, END)
    e2.delete(0,END)
    e1.focus_set()
window = Tk()
window.geometry("500x200")

u_frame = Frame(window, height=30)
u_frame.grid(row=0, columnspan=2)

frame = Frame(window, width=50)
frame.grid(column=0, row=1)

d_frame = Frame(window,width=300)
d_frame.grid(row=1,column=1)

Label(d_frame, text="ID").grid(row=0, column=0, padx=20)
Label(d_frame, text="PASSWORD").grid(row=1, column=0)

e1 = Entry(d_frame, font=('맑은고딕', 15), fg='#1F50B5')
e2 = Entry(d_frame, font=('맑은고딕', 15), fg='#1F50B5', show='*')

e1.grid(row=0, column=1, ipady=5, pady=5)
e2.grid(row=1, column=1, ipady=5, pady=5)

Button(d_frame, text="로그인", font=('맑은고딕', 10), command=show).grid(row=0, column=2, rowspan=2, padx=00, pady=0, ipadx=5, ipady=30)


window.mainloop()