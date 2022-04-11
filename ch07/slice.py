aa = [10, 20, 30, 40, 50, 60, 70]

# 10, 20, 30
print(aa[:3])

# 10
print(aa[:1])

# 30, 40
print(aa[2:])

# ERROR
print(aa[3:-3])

# 40
print(aa[3:])

# 10, 20, 30
print(aa[:-2])

print('=====STEP=====')
# step
print(aa[::2])
# 역순으로 출력
print(aa[::-1])
print(aa[::-2])

print('=====리스트 값 변경=====')
bb = [10, 20, 30]
print(bb)
bb[1:2] = [200, 201]
print(bb)

# [1:2]와 [1]의 차이점 알기
bb[1] = [200, 201]
print(bb)

# 삭제
bb[1:2] = []
print(bb)

# 리스트 내용 삭제
bb = [];

print(type(bb))













