# 100 Days of code by Angela Yu
# Day 2 - Tip Calculator

print("Welcome to the tip calculator!")
bill_amount = float(input("What was the bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12 or 15? "))
group_size = int(input("How many people to split the bill? "))

bill_total = bill_amount + (bill_amount * (tip_percent / 100))
bill_share = round(bill_total / group_size, 2)

print(f"Each person sould pay: ${bill_share:.2f}")
