# 100 Days of code by Angela Yu
# Day 1 - Band Name Generator

import tkinter as tk

FONT_TITLE = tk.font=("Arial", 20, "bold")

def create_name():
    city = city_entry.get()
    pet = pet_entry.get()

    band_name = f"{city} {pet}"

    band_label.config(text=band_name)

root = tk.Tk()
root.title("Band name generator")

label_title = tk.Label(root, text="Create your band name!", font=FONT_TITLE)
label_title.pack()

city_label = tk.Label(root, text="Name of city where you grow up:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

pet_label = tk.Label(root, text="Name of your childhood pet:")
pet_label.pack()
pet_entry = tk.Entry(root)
pet_entry.pack()

create_button = tk.Button(root, text="Create name", command=create_name)
create_button.pack()

band_label= tk.Label(root, text="--------")
band_label.pack()

root.mainloop()

"""
city = input("Name of the city where you grow up: ")
pet = input("Name of your childhood pet: ")


print(f"Your Band name is: {city} {pet}")
"""