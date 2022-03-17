import random
import turtle

# 함수 정의

def screeenLeftClick(x, y):
    tSize = random.randrange(2, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r, g, b))
    tAngle = random.randrange(0, 360)

    turtle.penup()
    turtle.goto(x, y)
    turtle.left(tAngle)
    turtle.stamp()

tSize, tAngle = 0, 0
r, g, b = 0.0, 0.0, 0.0

turtle.title("Turtle Test")
turtle.shape('turtle')

turtle.onscreenclick(screeenLeftClick, 1)

turtle.done()