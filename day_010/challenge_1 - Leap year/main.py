# 100 Days of code by Angela Yu
# Day 10 - Challenge 1 - Leap year

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    # Write your code here. 
    # Don't change the function name.



print(is_leap_year(2001))