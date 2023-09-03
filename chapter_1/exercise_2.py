from matplotlib import pyplot as plt
import numpy as np
import csv
dev_x = [23, 24, 25, 26, 27, 28, 29]
dev_y = [2233, 2244, 2266, 2345, 2456, 2533, 2678]
ages_def_y = [2354, 2754, 2322, 2844, 2354, 2544, 2456,]
name_def_y = [2345, 2355, 2356, 2433, 2435, 2444, 2533,]
x_indexes = np.arange(len(dev_x))
width = 0.25
plt.bar(x_indexes-width, dev_y, label = 'me', width=width, color = '#4444',)
plt.bar(x_indexes+width, ages_def_y, width=width, label = 'you', color = 'g')
plt.bar(x_indexes, name_def_y, width=width, label = 'name', color = 'r')
plt.xlabel('ages')
plt.ylabel('median salary (usd)')
plt.title('midian salary by USD')
plt.xticks(ticks=x_indexes, labels=dev_x)
plt.tight_layout()
plt.grid(True)
plt.legend()


plt.show()
