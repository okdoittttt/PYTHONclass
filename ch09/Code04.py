from matplotlib import pyplot as plt

y = [5, 3, 7, 10, 11, 20]
x = range(len(y))

# 그래프 바로 표현
# plt.bar(x, y, width=0.7, color="blue")
# plt.show()

# 그래프 선으로 표현
plt.plot(x, y, color="red")
plt.scatter(x, y, linewidths=5, color="red")
plt.grid(True)
plt.show()
