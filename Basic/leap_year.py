def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 ==0 :
        if year % 100 != 0 or year % 400 ==0:
            leap = True
    else:
        leap = False    
    return leap
year = int(input("Enter Year"))
leap = is_leap(year)
if leap == True:
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
