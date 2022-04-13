# 변수 정의
nameList = ['홍길동', '허봉식', '손옥무']

# 함수 정의
def selfintro():        # 함수로 출력
    print("안녕하세요.")
    print("저는 동의과학대학교 학생입니다.")

def sayName(name):      # 매개변수 받아 출력
    print("안녕하세요, {}씨".format(name))

def sayHelloIntro(name):        # 함수를 함수로 묶기
    selfintro()
    sayName(name)

def quickSay(names):        # list로 출력하기
    for item in names:
        sayHelloIntro(item)

def intro(name, age):       # 여려 매개변수 받기
    print("안녕하세요 저는 {}세, {}입니다.".format(age, name))

def myFruits(*fruits):    # 호출시 넘겨지는 인수들은 리스트에 담긴다.
    for item in fruits:
        print("I like {}.".format(item))

def intro2(countury = 'Korea'):     # 매개변수에 default값 주기
    print("I'm from {}".format(countury))

def mulFive(num):
    return num * 5


# 함수 호출
sayHelloIntro('홍길동')
quickSay(nameList)
intro('이순신', 29)
intro(age=21, name='홍길동')
myFruits('apple', 'kiwi', 'mango', 'melon', 'banana')
intro2()
intro2('Japan')
print(mulFive(5))












