# Here we plot bar graph
import matplotlib.pyplot as plt

plt.bar([1, 3, 5, 7, 9],[5, 2, 7, 8, 2], label = 'Example 1')
plt.bar([2, 4, 6, 8, 10],[1, 3, 5, 7, 9], label = 'Example 2', color = 'g')
plt.legend()
plt.title('Bar-Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()

