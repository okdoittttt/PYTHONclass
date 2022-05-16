import random as rm

# random number 추출
def randomNumber():
    return rm.randrange(1, 46)

lotto = [0,0,0,0,0,0,0]
num = 0

print("로또 번호 추출을 시작합니다.")

for i in range(1, 7):
    num = randomNumber()
    lotto[i] = num
    print("lotto 번호 %d"%lotto[i])

