with open('chapter_9/grade_book.txt', mode='r') as grade_reader:
    for content in grade_reader:
        name, score = content.split()
        print(score)