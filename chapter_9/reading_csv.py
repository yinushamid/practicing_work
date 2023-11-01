import csv 
with open('write_practise.csv', mode = 'w', newline='') as my_file:
    writer = csv.writer(my_file)
    writer.writerow([1, 'for', 'one'])
    writer.writerow([2, 'for', 'two'])
    writer.writerow([3, 'for', 'three'])
    writer.writerow([4, 'for', 'four'])
    