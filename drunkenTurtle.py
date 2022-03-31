import turtle as t
import random

# 변수 선언
swidth, sheight, x, y, angle, outCount, dist, locateX, locateY = 300, 300, 0, 0, 0, 0, 0, 0, 0
r, g, b = 0, 0, 0

# Turtle 정의
t.shape('turtle')
t.speed(5)
t.pensize(3)

# 함수 정의
while True:
    # turtle 랜덤 방향, 거리 배정
    angle = random.randrange(0, 360)
    dist = random.randrange(0, 100)
    t.left(angle)
    t.fd(dist)
    locateX = t.xcor()
    locateY = t.ycor()

    # turtle 랜덤 색상 배정
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor((r, g, b))

    # turtle 종료 조건

t.done()
