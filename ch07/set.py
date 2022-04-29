set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1&set2)

numList = [num for num in range(1, 11) if num % 3 == 0]
print(numList)

a = ['name', 'age', 'gender']
b = ['son', '20', 'male']
c = dict(zip(a,b))

print(c)

aa = ['a', 'b', 'c', 'd', 'e']
bb = [1, 2, 3]

for s in zip(aa, bb):
    print(s)
    print(list(s))

x = ['a', 'b', 'c']
y = [1, 2, 3]
d = []

for i, j in zip(x, y):
    d.append(i)
    d.append(j)

print(d)