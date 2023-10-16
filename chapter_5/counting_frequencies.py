import numpy as np
values = list(np.random.randint(1, 10, 20))
name =np.unique(values, return_counts=True)
print(name)