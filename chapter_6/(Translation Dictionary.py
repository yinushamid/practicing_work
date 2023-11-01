# Create a translations dictionary that maps theEnglish words to their translations with ebira
ebira_translation_dictionary = {'name' : 'ireha', 'wife' : 'ose', 'penis' : 'anapa', 'male' : 'onoru'}
print('english          ebira translation')
for english, name in ebira_translation_dictionary.items():
    print('{0:<23}{1}'.format(english, name))