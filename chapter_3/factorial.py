def factorials(n):
    factorial = 1 # initialise factorial = 1 to keep track of nth terms
    '''iterate through the n factorial in descending order'''
    for num in range(n, -1, -1):
        '''use if statement to return 1 whenever n == 0 to avoid 0 answer for 0 factoria'''
        if num == 0:
            num = 1
        
        factorial *= num
    return factorial    
print(factorials(10))