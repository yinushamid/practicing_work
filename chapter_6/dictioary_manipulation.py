dictionary_manipulates = {'nigerial' : 'niger', 'america' : 'usa', 'saudi arabia' : 'UAE', 'isreal' : 'killers'}
# Check whether the dictionary contains the key 'isreal'.
if 'isreal' in dictionary_manipulates.keys():
    print('isreal is there')
else:
    print(None)

# Check whether the dictionary contains the key 'France'.
if 'america' in dictionary_manipulates.keys():
    print('america is there')
else:
    print(None)

# Iterate through the key–value pairs and display them in two column format.
print('country             name')
for country, name in dictionary_manipulates.items():
    
    print('{0:<20}{1}'.format(country, name))

# #  Add the key–value pair 'Sweden' and 'sw' (which is incorrect)
# print(dictionary_manipulates['sweden'])

#  Use a dictionary comprehension to reverse the keys and values.
country_names = [{name: country for country, name in dictionary_manipulates.items()}]
print(country_names)

# use a dictionary comprehension to convert the country names to all uppercase letters.
country_names = {name: country for country in dictionary_manipulates.items()}
print({name.upper(): country for name, country in dictionary_manipulates.items()})
