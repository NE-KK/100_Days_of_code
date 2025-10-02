# 100 Days of code by Angela Yu
# Day 8 - Challenge 1 - Weeks in Life

def weeks_in_life(age: int) -> int:
    years_left = 90 - age
    return years_left * 52


age = int(input("What is your current age in years? "))

weeks_to_live = weeks_in_life(age)
print(f"There are {weeks_in_life} weeks left!")