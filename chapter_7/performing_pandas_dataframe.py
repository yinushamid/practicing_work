import pandas as pd
#  Create a DataFrame named temperatures from a dictionary of three temperature readings each for 'Maxine','James' and 'Amanda'.
temperature = {'maxine': [30, 41, 50], 'james' : [43, 32, 50], 'amanda' : [51, 40, 30]}
print(pd.DataFrame(temperature))
#  Recreate the DataFrame temperatures in Part (a) withcustom indices using
#  the index keyword argument and a list containing 'Morning', 'Afternoon' and 'Evening
temperature = {'maxine': [30, 41, 50], 'james' : [43, 32, 50], 'amanda' : [51, 40, 30]}
print(pd.DataFrame(temperature, index = ['morning', 'afternoon', 'night']))
# Select from temperatures the column of temperaturereadings for 'Maxine'.
print(temperature['maxine'])
