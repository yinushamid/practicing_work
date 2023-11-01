import math 
total = 0
with open('chapter_9/grade_book.txt', mode='r') as grade_reader:
    for items in grade_reader:
        name, mark = items.split()
        print(math.fsum(int(mark)))

    
