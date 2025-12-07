# 100 Days of code by Angela Yu
# Day 2 - Tip Calculator

from tkinter import *
from tkinter import ttk


def calculate_bill():
    bill = float(bill_entry.get())
    percent = int(tip_entry.get()) / 100
    bill_share = int(share_entry.get())
    final_bill = bill + (bill * percent)
    final_price_per_person = final_bill / bill_share

    bill_result = Tk()
    bill_result.title("Result")
    bill_result.geometry("300x160")

    result_label = ttk.Label(bill_result, text=f"The Total bill is: ${final_bill:.2f}")
    result_label.pack()
    per_person_label = ttk.Label(bill_result, text=f"Each person should pay: ${final_price_per_person:.2f}")
    per_person_label.pack()

    bill_result.mainloop()


root = Tk()
root.title("Tip Calculator")
root.geometry("300x160")

frame_bill = ttk.Frame(root, padding=10).pack()
frame_tip = ttk.Frame(root, padding=10).pack()
frame_share = ttk.Frame(root, padding=10).pack()


ttk.Label(frame_bill, text="What was the bill? in $").pack()
bill_entry = ttk.Entry(frame_bill)
bill_entry.pack()

ttk.Label(frame_tip, text="How much do you tip? in %").pack()
tip_entry = ttk.Entry(frame_tip)
tip_entry.pack()

ttk.Label(frame_share, text="How many people share the bill?").pack()
share_entry = ttk.Entry(frame_share)
share_entry.pack()

ttk.Button(root, text="Calculate", command=calculate_bill).pack()

root.mainloop()
