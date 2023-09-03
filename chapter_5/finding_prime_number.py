def find_prime_number(n):
    # initialise all number to true
    number = [True] * n
    # assign 0 and 2 not a prime number
    number[0] = number[1] = False
    #iterate through all elemrnt
    for num in range(n):
        #remove all element thats not prime number
        if number[num]:
            for even in range(num*num, n, num):
                number[even] = False
     #print prime number           
    for num in range(n):
        if number[num]:
            print(num)

find_prime_number(1000)




    
