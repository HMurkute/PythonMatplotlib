from matplotlib import pyplot as plt
# Here we first define variables x and y and then we plot them.

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 6, 8, 10, 12]

plt.plot(x, y)

plt.title('Info')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')

plt.show()
