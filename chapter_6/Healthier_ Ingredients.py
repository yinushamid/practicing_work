
healthier_replacement = {'1 cup of milk': 'breast milk', '1 cup of sugar': 'botttle of honey', '1 cup of rice': '1 cup of beans', '1 cup of water': 'half cup of water'}
ingredient = input('choose your ingredient:  ')
print('ingredient                          substitution')
for key, value in healthier_replacement.items():
    if key == ingredient:
        print('{0}{1:>35}'.format(key, value))
