import random
import turtle

col = ["red", "blue", "orange", "black", "white", "gray", "yellow", "pink"]

# print list
print(col)
# print list index
print(col[0])
# print list index length
print("Length = ", len(col[0]))
# print type
print(type(col))

# 0~7까지 랜덤으로 숫자 추출
ind = random.randint(0, 7)
print(ind)
turtle.bgcolor(col[ind])

def fxn(x, y):
    global col
    # ["white", "white", "white"]
    ind = random.randint(0, 7)
    turtle.bgcolor(col[ind])
    print(x, y)

#turtle setup
turtle.setup(400, 300)

turtle.onscreenclick(fxn, 1)
# turtle 실행
turtle.done()
