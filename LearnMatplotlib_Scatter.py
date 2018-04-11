import matplotlib.pyplot as plt

x = [i for i in range(1,9)]
y = [5, 2, 4, 2, 1, 4, 5, 2]

plt.scatter(x, y, label='skitscat', color='k')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()

plt.show()

