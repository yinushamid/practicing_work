# manipulate sets
first = {'red', 'green', 'blue'}
second = {'cyan', 'green', 'blue', 'magenta', 'red'}
# comparing the sets using the each of the comparison operators.
print(first == second)
print(first.issuperset(second))
print(first.issubset(second))
print(first.isdisjoint(second))
#  combining the sets using each of the mathematical set operators
print(first.union(second))
print(first.intersection(second))
print(first.difference(second))
