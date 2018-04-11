import matplotlib.pyplot as plt

slices = [7, 2, 2, 13]

activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['c', 'm', 'r', 'b']

plt.pie( slices,
         labels=activities,
         colors=colors,
         startangle=90,
         shadow=True, # This make slices have shadows.
         explode=(0.1, 0.2, 0.3, 0.4),  # This function does the work that it makes the slices come out a little according to the value.
         autopct='%1.1f%%')  # This function makes the percentage of area covered by the slices makes appear on them like format described in the code.

plt.title('Pie Chart')
plt.show()

