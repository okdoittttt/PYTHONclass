a = int(input('1. 입력한 수식 계산 2. 두 수 사이의 합계'))

resut = 0

if a == 1:
    eval1 = input('수식 입력 : ')
    result = eval(eval1)
    print(result)
elif a == 2:
    num1 = int(input('첫 번째 정수 입력 : '))
    num2 = int(input('두 번째 정수 입력 : '))
    for i in range(num1, num2+1):
        result = result + i

    print(result)
