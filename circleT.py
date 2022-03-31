import turtle as t
import random

t.shape('turtle')
t.pensize(3)
t.speed(3)

def turtleClick(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(50)
    t.color("black")

def randomTurtle(x, y):
    t.pencolor("red")
    for _ in range(50):
        rx = random.randrange(-600, 600)
        ry = random.randrange(-600, 600)
        print("x = ",rx,"y = ",ry)
        t.penup()
        t.goto(rx, ry)
        t.pendown()
        t.circle(50)

# t.onscreenclick(turtleClick, 1)
t.onscreenclick(randomTurtle, 1)

t.done()