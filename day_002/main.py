# 100 Days of code by Angela Yu
# Day 2 - Tip Calculator

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tip calculator")
root.geometry("300x200")

frm_bill = ttk.Frame(root, padding=10)
frm_bill.grid(column=0, row=0)

ttk.Label(frm_bill, anchor="w", justify="left", text="What was the bill? $").grid(column=0, row=0)
ttk.Entry(frm_bill,).grid(column=1, row=0)

frm_percent = ttk.Frame(root, padding=10)
frm_percent.grid(column=0, row=1)

ttk.Label(frm_percent, text="Tips you like to give? %", justify="left").grid(column=0, row=0)
ttk.Entry(frm_percent, ).grid(column=1, row=0)


root.mainloop()


"""
print("Welcome to the tip calculator!")
bill_amount = float(input("What was the bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12 or 15? "))
group_size = int(input("How many people to split the bill? "))

bill_total = bill_amount + (bill_amount * (tip_percent / 100))
bill_share = round(bill_total / group_size, 2)

print(f"Each person sould pay: ${bill_share:.2f}")
"""