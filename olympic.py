# 올림픽 오륜기 그리기.
import turtle as t

# turtle의 속도, 펜 사이즈 선언.
# 검정색(2번) 원
t.speed(0)
t.pensize(20)

t.circle(100)

# 붉은색(3번) 원
t.up()
t.forward(240)
t.down()
t.pencolor('red')
t.circle(100)

# 푸른색(1번) 원
t.up()
t.backward(480)
t.down()
t.pencolor('blue')
t.circle(100)

# 노란색(4번) 원
t.up()
t.right(90)
t.forward(120)
t.left(90)
t.forward(120)
t.down()
t.pencolor('yellow')
t.circle(100)

# 초록색(5번) 원
t.up()
t.forward(240)
t.down()
t.pencolor('green')
t.circle(100)

t.done()