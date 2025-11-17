# 100 Days of code by Angela Yu
# Day 5 - Challenge 3 - FizzBuzz

# Rules:
#   if number % 3 == 0 print Fizz
#   if number % 5 == 5 print Buzz
#   if number % 3 == 0 and number % 5 == 0 print FizzBuzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
