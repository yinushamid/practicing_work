import numpy as np
integers = np.arange(225)
print('integers                corresponding alphabet')
for integer in integers:
    print('{0}{1:>28}'.format(integer, chr(integer)))
