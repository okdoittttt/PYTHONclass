import random
import turtle

# 함수 정의

def screenLeftClick(x, y):
    global r, g, b

    r = random.random()
    g = random.random()
    b = random.random()

    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)

    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)

def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)

# 변수 선언

pSize = 10
r, g, b = 0.0, 0.0, 0.0

# Turtle 정의, 실행

turtle.title('Turtle Graphic')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 2)

turtle.done()
