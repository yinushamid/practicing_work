# create a function call palindrone
def is_palindrone(sentence):
    # initialise a variable to add all selected characters
    string = ""
    # initialise for loop tonkeep track all characters and select all alphas
    for character in sentence:
        if character.isalpha():
            string += character
            # return palindrones characters
    return string[::-1] == string[:]
    
# prompt the users to test for palindrone words
word = input('enter a word to check:  ')
if  is_palindrone(word):
    print('"{}" is a palindrone'.format(word))
else:
    print('"{}" is not a palindrone'.format(word))