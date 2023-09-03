from matplotlib import pyplot as plt
data = [20, 40, 35, 50]

label = ['chelsea', 'mancity', 'arsenal', 'liverpool']
color = ['blue', 'red', 'green', 'pink']
plt.title('club value statistics pie chart')
plt.pie(data, labels=label, colors=color,  shadow=True, autopct='%1.1f%%')
plt.show()
