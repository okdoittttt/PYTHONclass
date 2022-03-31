
while True:
    a = input('정수 입력 : ')

    if a == 'q':
        break
    else:
        a = int(a)
        if a%2 == 0:
            print('짝수입니다.')
        elif a%2 > 0:
            print('홀수입니다.')