from itertools import permutations
names = permutations(['a','n', 'a', 'g', 'r', 'a', 'm'], 4)
for name in names:
    print(name)