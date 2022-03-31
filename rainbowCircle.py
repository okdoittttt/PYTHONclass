import turtle as  t
import random

swidth, sheight = 500, 500
r, g, b = 0, 0, 0

t.shape('turtle')
t.speed(100)
t.pensize(0.3)
t.setup(width=swidth+50, height=sheight+50)
t.screensize(swidth, sheight)

for i in range(0, 250, 1):
    t.pendown()
    t.circle(i)
    t.penup()
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor((r, g, b))

t.done()