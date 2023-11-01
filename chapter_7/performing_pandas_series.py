import pandas as pd
import numpy as np
# Create a Series from the list [7, 11, 13, 17].
lists = [7, 11, 13, 17]
print(pd.Series(lists))
# Create a Series with five elements that are all 100.0.
print(pd.Series(100, range(5)))
# Create a Series with 20 elements that are all random numbers in the range 0 to 100.
#  Use method describe to produce the Series’ basic descriptive statistics.
series  = np.random.randint(0, 100, 20)
print(series)
#  Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9. Using the index
# keyword argument, specify the custom indices 'Julie',
# 'Charlie', 'Sam' and 'Andrea'.
list = [98.6, 98.9, 100.2, 97.9]
print(pd.Series(list, index=['Julie','Charlie', 'Sam', 'Andrea']))
# Form a dictionary from the names and values in Part (d), then useit to initialize a Series.
dictionary = {'man' : 'woman', 'boy': 'girl', 'male': 'female'}
print(pd.Series(dictionary))