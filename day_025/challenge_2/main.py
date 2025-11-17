# 100 Days of code by Angela Yu
# Day 25 - Challenge 2 - Squirrel Data Analysis


import pandas
data = pandas.read_csv("squirrel_data.csv")
"""
color_cinnamon = 0
color_gray = 0
color_black = 0

color_list = data["Primary Fur Color"]

for color in color_list:
    if color == "Gray":
        color_gray += 1
    if color == "Black":
        color_black += 1
    if color == "Cinnamon":
        color_cinnamon += 1

print(f"Gray: {color_gray}")
print(f"Black: {color_black}")
print(f"Cinnamon: {color_cinnamon}")
"""
print(data.value_counts("Primary Fur Color"))
