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