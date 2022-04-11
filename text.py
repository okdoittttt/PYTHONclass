# s = input("문자열 입력 : ")
# cup = ""
# spacebar = " "
# cup2 = ""
#
# print(s)
# print("====================")
# for i in s:
#     cup += i
#     print("%s"%cup)
#
# print("====================")
# for j in s:
#     print(cup2, j)
#     cup2 += spacebar


# ==================== if else 문 ====================
# 정수를 입력받아 양수이면 홀/짝 여부를 출력, 아니면 "양수를 입력하세요"라고 출력

# num = int(input("정수를 입력하세요."))
#
# if num > 0:
#     if num%2 == 0:
#         print("짝수입니다.")
#     else:
#         print("홀수입니다.")
# else:
#     print("양수를 입력하세요.")

# 1~10 범위의 수를 입력, 소수면 '소수', '수수가 아님', '잘못된 입력' 출력하기

# 방법 1번
# num = int(input("1~10 사이의 수를 입력하시오."))

# if num == 2 or num == 3 or num == 5 or num == 7:
#     print("소수 입니다.")
# elif num == 1 or num == 4 or num == 6 or num == 8 or num == 9 or num == 10:
#     print("소수가 아닙니다.")
# else:
#     print("잘못된 입력")

# 방법 1번 (1~10까지의 정수인지 판별한 후, 2부터 자기 자신까지 수를 계속 나누어 0이 되는지 확인.)
# num = int(input("정수를 입력하세요."))
# b = 0
#
# if num <= 10:
#     for i in range(2, num):
#         if num % i == 0:
#             b = 1
#     if b == 0:
#         print("소수입니다.")
#     else:
#         print("소수가 아닙니다.")
# else:
#     print("잘못된 입력입니다.")

# 문자열에서 특정 문자 찾기
# first = "김현준강문호권기훈김수린김신영홍서현김민지허윤조상원최다령"
# second = "박재용이주명오유경정승찬손옥무김민석장성익이로겸설재혁이태윤김건우"
# prof = "김종현김진숙백건효허봉식"
#
# name = input("이름을 입력하세요.")
#
# if name in first:
#     print("1학년")
# elif name in second:
#     print("2학년")
# else:
#     print("교수")

# collection 자료형

# a = {'name':'son', 'age':'27'}
# print(a)
#
# for i, v in a.items():
#     print("%s %s"%(i, v))

# 딕셔너리 출력하기.
data = {
    "철수": 98,
    "영희": 80,
    "순이": 100,
    "돌이": 70,
}
sum = 0
for name, score in data.items():
    print("%s %10.d"%(name, score))
    sum = sum + score
print("================")
print("평균 %10.f"%(sum/len(data)))













