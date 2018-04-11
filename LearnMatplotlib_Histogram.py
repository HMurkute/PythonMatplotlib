import matplotlib.pyplot as plt

population_ages = [36, 28, 38, 46, 55, 68, 72, 55, 36, 38, 67, 45, 22, 48, 91, 46, 52, 61, 58, 55]
bins = [10*i for i in range(11)]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('Ages')
plt.ylabel('Frequency')

plt.title('Histogram')

plt.show()

