a = 'happy'
b = ""

for i in range(len(a)):
    b += a[len(a)-i-1]

print(b)

# print(a[::-1])