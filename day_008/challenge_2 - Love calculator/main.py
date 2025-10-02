# 100 Days of code by Angela Yu
# Day 8 - Challenge 2 - Love Calculator

def love_score(name_1, name_2):
    names = (name_1 + name_2).lower()

    num1_t = names.count("t")
    num1_r = names.count("r")
    num1_u = names.count("u")
    num1_e = names.count("e")
    first_number = (num1_t + num1_r + num1_u + num1_e)

    num2_l = names.count("l")
    num2_o = names.count("o")
    num2_v = names.count("v")
    num2_e = names.count("e")
    second_number = (num2_l + num2_o + num2_v + num2_e)
    
    return str(first_number) + str(second_number)



# first name
person_1 = input("What is the name of the first person: ")
person_2 = input("What is the name of the first person: ")

calculated_score = love_score(person_1, person_2)
print(f"The love score is: {calculated_score}")
