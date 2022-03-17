# turtle을 이용한 펜 기능 만들기.
import random
import turtle

# 함수 정의
# r, g, b는 전역변수로 선언
# random으로 생성한 수를 통해 색상, 크기 결정.

# 왼쪽 마우스 클릭시 turtle의 색상, 크기, 위치 변경.
# turtle을 이동시킴과 동시에 pendown()하여 이동경로 표시.
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

# penup()을 통해 이동경로 표시 중단.
# 클릭시 turtle의 이동만 진행.
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
