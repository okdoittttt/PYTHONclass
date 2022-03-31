s = input("문자열 입력 : ")
cup = ""
spacebar = " "
cup2 = ""

print(s)
print("====================")
for i in s:
    cup += i
    print("%s"%cup)

print("====================")
for j in s:
    print(cup2, j)
    cup2 += spacebar
