import random
"""guesing number of range 1 to 1000"""
def guess_number():
    # use random function to choose and hide the number to guess
    guessnumber = random.randint(1, 1000)
    # initialise while loop to prompt and keep track of guess number
    while True:
        guess = int(input('enter any number from 1 to 1000: '))
        # use if statement to 
        if guess > guessnumber:
            print("your guess is too high, TRY AGAIN:")
        elif guess < guessnumber:
            print("your guess is too low, TRY AGAIN:")
        else: 
            print('CONGRATULATION.  you guessed the number')
            break
        guess_number()
guess_number()    

