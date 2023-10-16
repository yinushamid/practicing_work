'''create a function that find all even numbers and assign odd numbers to false'''
def multiple(n):
    # make all element in the numbers to be true first
    number = [True] * n
    #assign element 1 and 2 to be false
    number[0] = number[1] = False
    #iterate through all element
    for num in range(n):
        #remove some non multiple of 3 element

        if number[num]:
            for i in range(n):
                if i % 3 != 0:
                    number[i] = False
     # print the multiple of three         
    for num in range(n):
        if number[num]:
            print(num)

multiple(100)