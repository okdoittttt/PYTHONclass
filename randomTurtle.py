# 화면을 클릭하면 터틀의 크기, 색상, 위치를 변경시키는 프로그램.
import random
import turtle

# 함수 정의
# turtle의 사이즈를 random()을 통해 설정.
# r, g, b 색상을 random()를 통해 설정.
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

# 변수 선언
# 가본값은 모두 0으로 초기화.
tSize, tAngle = 0, 0
r, g, b = 0.0, 0.0, 0.0

turtle.title("Turtle Test")
turtle.shape('turtle')

turtle.onscreenclick(screeenLeftClick, 1)

turtle.done()