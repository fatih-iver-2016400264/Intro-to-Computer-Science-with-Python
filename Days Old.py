# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]
    
    if isLeap(year1):
        daysOfMonths[1] = 29
    else:
        daysOfMonths[1] = 28
    
    if year1 == year2:
        return (daysOfMonths[month1-1] - day1) + sum(daysOfMonths[month1:month2-1]) + day2

    totalDays = 0
    
    for year in range(year1, year2 + 1):
        
        if isLeap(year):
            daysOfMonths[1] = 29
        else:
            daysOfMonths[1] = 28
        
        if year == year1:
            totalDays += (daysOfMonths[month1-1] - day1) + sum(daysOfMonths[month1:]) 
        elif year == year2:
            totalDays += day2 + sum(daysOfMonths[:month2 - 1])
        else:
            totalDays += sum(daysOfMonths)
    return totalDays
            

# Test routine

def isLeap(year):
    return (year % 100 == 0 and year % 400 == 0 ) or (year % 4 == 0 and year % 100 != 0)
    
    
    #if year % 4 == 0:
        #if year % 100 == 0:
            #if year % 400 == 0:
                #return True
            #else:
                #return False
        #return True
    #return False

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

#test()
print(daysBetweenDates(1973,7,28,2018,1,13))
