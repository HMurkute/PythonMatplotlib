# Here we plot full functional 2 lines comparison with different colors and width of lines and etc.

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [i for i in range(10)]
y = [i for i in range(10)]

x1 = [i for i in range(10)]
y1 = [2*i for i in range(10)]

plt.plot(x, y, 'g', label='Line 1',linewidth=5)
plt.plot(x1, y1,'c', label='Line 2',linewidth=5)

plt.title('Info')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.legend()

plt.grid(True,color='K')

plt.show()

