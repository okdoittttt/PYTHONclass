# 변수 선언
food = {"떡볶이":"어묵",
        "짜장면":"단무지",
        "치킨":"맥주"}

# 딕셔너리에 key와 values 출력하기.
for k in food.values():
    print(k)

for item in food.items():
    print(item)


# 메인 소스코드
while True:
    myFood = input(str(list(food.keys())) + "중 좋아하는 음식은 ?")
    if myFood in food:
        print("<%s> 궁합 음식은 <%s>"%(myFood, food.get(myFood)))
    elif myFood == '끝':
        break
    else:
        print("그런 음식이 없습니다.")