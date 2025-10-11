# 100 Days of code by Angela Yu
# Day 10 - Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def choose_calc():
    operation = input("Choose a calculation (+, -, *, /): ")
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))

    calculation = operation_dict[operation]

    print(calculation(num1, num2))


choose_calc()
