# 동전 교환 프로그램
# 입력받은 수(돈)가 500, 100, 10(원) 순서로 나누는 프로그램.

# 변수 선언
money, exchange, coin500, ex500, coin100, ex100, coin50, ex50, coin10, ex10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
i = 1
# 함수 정의
while i > 0:
    money = int(input("동전을 입력하세요."))

    coin500 = money / 500
    ex500 = money % 500

    coin100 = ex500 / 100
    ex100 = ex500 % 100

    coin50 = ex100 / 50
    ex50 = ex100 % 50

    coin10 = ex50 / 10
    ex10 = ex50 % 10

    exchange = ex10
    i = money

    print(int(coin500))
    print(int(coin100))
    print(int(coin50))
    print(int(coin10))
    print("나머지 금액 : ")
    print(ex10)


quit()
