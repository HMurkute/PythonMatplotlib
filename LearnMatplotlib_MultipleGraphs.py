import matplotlib.pyplot as plt
import numpy as np


def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)


t1 = np.arange(0, 5.0, 0.1)
t2 = np.arange(0, 5.0, 0.2)

plt.subplot(211) # The number code goes as follows : As here it is '211' first 2 means we have 2  graphs available with us and next 1
plt.plot(t1, f(t1), 'bo', t2, f(t2)) #  means only one graph in horizontal and next 1 means this is the 1st graph


plt.subplot(212) # As here stated that '212' means that 2 means that 2 graphs are available with us next 1 means that one is horizontally present
plt.plot(t2, np.cos(2*np.pi*t2)) # and next 2 means this is the 2nd graph.
plt.show()

