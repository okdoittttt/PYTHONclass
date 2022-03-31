import turtle
import random


class Shape:
    def __init__(self):
        self.myTurtle = turtle.Turtle('turtle')

    def setPen(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r, g, b))
        pSize = random.randrange(1, 10)
        self.myTurtle.pensize(pSize)


class Rectangle(Shape):
    def __init__(self, x, y):
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)

    def drawShape(self):
        sx1 = self.cx - self.width / 2
        sy1 = self.cy - self.height / 2
        sx2 = self.cx + self.width / 2
        sy2 = self.cy + self.height / 2

        self.setPen()
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)


class Circle(Shape):

    def __init__(self, x, y):
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        self.radius = random.randrange(20, 100)

    def drawShape(self):
        self.setPen()
        self.myTurtle.penup()
        self.myTurtle.goto(self.cx, self.cy)
        self.myTurtle.pendown()
        self.myTurtle.circle(self.radius)


def screenLeftClick(x, y):
    shape = random.randrange(0, 2)
    if (shape == 0):
        s = Rectangle(x, y)
    else:
        s = Circle(x, y)
    s.drawShape()


turtle.title('도형그리기')
turtle.onscreenclick(screenLeftClick)
turtle.done()