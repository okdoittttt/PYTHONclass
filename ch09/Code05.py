list = [1, 2, 3, 4, 5]

add = lambda num : num +20

for i in range(len(list)):
    list[i] = add(list[i])

print(list)