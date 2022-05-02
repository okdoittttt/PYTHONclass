import tkinter as tk
import turtle as t

swidth, sheight = 300, 300
txtSize = 30
t.shape('turtle')
t.setup(swidth + 50, sheight + 50)
t.screensize(swidth, sheight)

str = tk.simpledialog.asking('input char', 'input for turtle')