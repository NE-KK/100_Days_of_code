# 100 Days of code by Angela Yu
# Day 26 - challenge 2 - List Comprehensions filtering even numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
