class Car:
    color = ""
    speed = 0
    model = ""
    count = 0

    # 생성자 함수.
    def __init__(self, color, speed, model):
        self.color = color
        self.speed = speed
        self.model = model
        Car.count += 1

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -+ value

## main code
sonata = Car('red', 100, 'SONATA')
avante = Car('blue', 90, 'AVANTE')


print("%s의 색상은 %s 이며 속도는 %d 입니다. [총 생상량 : %d]"%(sonata.model, sonata.color, sonata.speed, Car.count))