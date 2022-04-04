# list 선언
fruit = ['apple', 'banana', 'orange', 'melon']
# list 가장 뒤에 요소 추가
fruit.append('kiwi')
# list의 길이 보기
print(len(fruit))
# list 마지막 요소 삭제
fruit.pop()
# list의 길이 보기
print(len(fruit))

# list의 index와 요소 출력
for i in fruit:
    print(fruit.index(i), i)

# list에 조건(요소)가 있으면 Yes, 없다면 No 출력
if 'banana' in fruit:
    print("Yes")
else:
    print("No")