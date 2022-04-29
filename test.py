stu = {"철수":90,
       "영희":80,
       "옥무":77,
       "선미":14}

sum = 0
avg = 0
for k in stu.keys():
    print("%s %10d"%(k, stu[k]))
    sum += stu[k]

avg = sum / 4
print("===============")
print("합계 %10d"%(avg))