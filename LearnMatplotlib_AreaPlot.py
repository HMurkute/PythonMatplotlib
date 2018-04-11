import matplotlib.pyplot as plt

days = [i for i in range(1,6)]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 3]

# Here we plotted blank lines just for sake of legends i.e we will get the labels.
plt.plot([],[], color='m', label='sleeping', linewidth=5)
plt.plot([],[], color='c', label='eating', linewidth=5)
plt.plot([],[], color='r', label='working', linewidth=5)
plt.plot([],[], color='k', label='playing', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Area Plot') # We call this type of chart a stack plot or Area plot
plt.legend()

plt.show()

