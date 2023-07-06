'''return time all in second'''
#initialise a function called seconds_since_midnight and pass hour, minute and second as argument
def seconds_since_midnight(hour, minute, second):
    # initialise variables to convert hours and minute to second
    hours_second = 3600*hour
    minute_second = 60 * minute
    # use if statement to valid the number from 0 to 60 minute and 0 to 24hours
    if hour > 0 and hour < 24:
        if minute > 0 and minute < 60: 
            
            return second + hours_second + minute_second
print(seconds_since_midnight(13, 44, 60))