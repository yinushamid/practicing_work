"""firstly import string to look for all alphabet words"""
import string

name = string.ascii_uppercase
'''initialise figure to keep track of all grouped alphabet'''
figure = 2
'''change the string alphabet to list so that you can perform some operation on iot'''
alphas = list(name)
"""initialise while loop to keep track all alphabet"""
while figure != 11:
    print(f"{figure}  {alphas[0:3]}")

    del alphas[0:3]
    figure += 1
    


