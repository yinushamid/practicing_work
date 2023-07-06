validation__number = ''
failures = 0

while validation__number != 1 and validation__number != 2:
    validation__number = int(input(' enter valid number:  '))
    if validation__number != 1 and validation__number != 2:
        failures +=1

    
print(f'the number of failures is  {failures}')
    
    


