# 100 Days of code by Angela Yu
# Day 2 - Tip Calculator

from tkinter import *
from tkinter import ttk


def calculate_bill():
    bill = int(bill_entry.get())
    percent = int(tip_entry.get()) / 100
    final_bill = bill + (bill * percent)

    bill_result = Tk()
    bill_result.title("Result")
    bill_result.geometry("300x160")

    result_label = ttk.Label(bill_result, text=f"The Total bill is: {final_bill:.2f}")
    result_label.pack()

    bill_result.mainloop()


root = Tk()
root.title("Tip Calculator")
root.geometry("300x160")

frame_bill = ttk.Frame(root, padding=10)
frame_bill.pack()
frame_tip = ttk.Frame(root, padding=10)
frame_tip.pack()

ttk.Label(frame_bill, text="What was the bill? in $").pack()
bill_entry = ttk.Entry(frame_bill)
bill_entry.pack()

ttk.Label(frame_tip, text="How much do you tip? in %").pack()
tip_entry = ttk.Entry(frame_tip)
tip_entry.pack()

ttk.Button(root, text="Calculate", command=calculate_bill).pack()


root.mainloop()



"""
print("Welcome to the tip calculator!")
bill_amount = float(input("What was the bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12 or 15? "))
group_size = int(input("How many people to split the bill? "))

bill_total = bill_amount + (bill_amount * (tip_percent / 100))
bill_share = round(bill_total / group_size, 2)

print(f"Each person should pay: ${bill_share:.2f}")
"""