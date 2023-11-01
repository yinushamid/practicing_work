with open('exercise_2') as names:
    title = '{0:<12}{1:<12}{2}'.format('turns', 'name', 'kilograms')
    logo = '*'
    print(title)
    logo*=len(title)
    print(logo)


    for name in names:
        turn, nam, kilo = name.split()
        
        print(f"{turn:<12}{nam:<12}{kilo}")
