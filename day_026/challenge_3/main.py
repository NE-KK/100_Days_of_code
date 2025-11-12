# 100 Days of code by Angela Yu
# Day 26 - challenge 3 - List Comprehensions compare files

file_1 = open("file1.txt", "r")
file_2 = open("file2.txt", "r")

num_list_1 = [int(i) for i in file_1]
num_list_2 = [int(i) for i in file_2]


result = [i for i in num_list_1 if i in num_list_2]

print(result)