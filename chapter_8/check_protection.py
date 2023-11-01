name = input('what is your name:  ')
format_name = "{0:0>15}".format(name)
newline = '-'
print(format_name)
newline *=len(format_name)
print(newline)
for figure in range(len(format_name)):
    print(figure, end='')
    













