from matplotlib import pyplot as plt
plt.xkcd()
dev_x = [23, 24, 25, 26, 27, 28, 29]
dev_y = [2233, 2244, 2266, 2345, 2456, 2533, 2678]
ages_def_y = [2344, 2254, 2322, 2344, 2354, 2444, 2456,]
name_def_y = [2345, 2355, 2356, 2433, 2435, 2444, 2533,]
plt.plot(dev_x, dev_y, label = 'me', color = 'b', linestyle = '--')
plt.plot(dev_x, ages_def_y, label = 'you', color = '0')
plt.plot(dev_x, name_def_y, label = 'name', color = 'r')
plt.xlabel('ages')
plt.ylabel('median salary (usd)')
plt.title('midian salary by USD')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.savefig('plot.png')

plt.show()


