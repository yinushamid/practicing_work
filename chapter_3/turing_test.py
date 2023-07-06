def medical_diagnosis(): # computer inteligent consultation
    question_1 = input('what is your problem: ')
    question_2 = input('have you had this problem before (yes or no):  ').lower()
    if question_2 == 'yes':
        print('WELL YOU HAVE IT AGAIN')
    elif question_2 == 'no':
        print('WELL YOU HAVE IT NOW')

    else:
        print('invalid input')

medical_diagnosis()
