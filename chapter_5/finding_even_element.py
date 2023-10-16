'''create a function that find all even numbers and assign odd numbers to false'''
def odd(n):
    # make all element in the numbers to be true first
    number = [True] * n
    #assign element 1 and 2 to be false
    number[0] = number[1] = False
    #iterate through all element
    for num in range(n):
        #remove the odd element
        if number[num]:
            for i in range(2, n, 2):
                number[i] = False
    for num in range(n):
        if number[num]:
            print(num)

odd(10)
