import random
def learn_multiplication( ):
    first_num = random.randint(1, 9)
    second_num = random.randint(1, 9)
    print(f'how much is the multiple of   {first_num}   and  {second_num}' )
    correct_answer = (first_num * second_num)
    student_answer = int(input('enter your answer:  '))
    if student_answer == correct_answer:
        outcome = 'very good', 'nice one', 'keep up the good work'
        random_answer = random.choice(outcome)
        print(random_answer)
    elif student_answer != correct_answer:
        outcome = 'no. please try again', 'wrong. put more effort', 'no. keep trying'
        random_answer = random.choice(outcome)
        print(random_answer)
print(learn_multiplication())
