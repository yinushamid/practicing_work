gallon_used = ''
total_gallon_used = 0 #initialise total gallon use to keep track of all gallon use 
total_mile_drive = 0 #initialise total mile drive to keep track of all mile drive 
'''loop through the  mile and gallon used and calculate mile per gallon use'''
while gallon_used != -1:
    gallon_used = int(input('enter the gallon used (-1 to end):  '))
    if gallon_used == -1: 
        break
    total_gallon_used += gallon_used
    mile_drive = int(input('enter the mile drive:  '))
    total_mile_drive += mile_drive
    mile_per_galon = mile_drive/gallon_used
    print(f'THE MILE FOR THIS GALLON IS {mile_per_galon.__round__(4)}mile')
'''initialise a variable called to calculate total mile drive per total gallon usedd'''
overall_mile_per_gallon = total_mile_drive/total_gallon_used
print(f'THE OVERALL MILE PER GAALLON IS {overall_mile_per_gallon.__round__(4)}mile')  
    
