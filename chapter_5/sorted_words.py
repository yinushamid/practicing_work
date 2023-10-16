def sort_words(name):
    alphabet = []
    
    for i in name:
        alphabet.append(i)
    if alphabet != sorted(name):
        print('its not a sorted word')
    else:
        print('its a sorted word')
sort_words('abcdef')