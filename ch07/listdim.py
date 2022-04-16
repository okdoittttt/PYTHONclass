# listRow = []
# listCol = []
#
# val = 1
#
# for i in range(0, 3):
#     for k in range(0, 4):
#         listRow.append(val)
#         val += 1
#     listCol.append(listRow)
#     listRow = []
#
# for i in range(0, 3):
#       for k in range(0, 4):
#             print("%3d" % listCol[i][k], end=" ")
#       print("")
# ==================================================================
# 2차원 배열 값 더하기
# aa = [[1, 2, 3, 4],
#       [5, 6],
#       [7, 8, 9]]
#
# totalsum = 0
#
# print(len(aa))
# for i in range(len(aa)):
#       sum = 0
#       for k in range(len(aa[i])):
#             sum += aa[i][k]
#             totalsum += aa[i][k]
#       print("{} Row : {}".format(i, sum))
#
# print("total : {}".format(totalsum))
# ==================================================================
# packing
num = (1, 2, 3, 4, 5)

# unpacking
v1,v2,v3,v4,v5 = num
print(v3)

x, y = 10, 20
x, y = y, x

print(x)
print(y)

print(type(x))
print(type(y))