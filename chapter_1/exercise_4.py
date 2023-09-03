import pandas as pd
from matplotlib import pyplot as plt
ages_x = [23, 34, 22, 45, 32, 33, 24, 41, 38, 26, 25, 21, 29]
bins = [20, 30, 40]
plt.hist(ages_x, bins=bins, edgecolor='red')
plt.xlabel('x_axes')
plt.ylabel('y_axis')
plt.title('my awesome histogram')
plt.show()