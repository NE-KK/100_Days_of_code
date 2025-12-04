# 100 Days of code by Angela Yu
# Day 1 - Band Name Generator

from tkinter import *
from tkinter import ttk


def generate_band_name():
    city_name = city_entry.get()
    pet_name = pet_entry.get()
    band_name = city_name + " " + pet_name

    window_band_name = Tk()
    window_band_name.title("Band name")
    window_band_name.geometry("250x50")

    ttk.Label(window_band_name, text="The Band name is:").pack()
    ttk.Label(window_band_name, text=band_name).pack()


root = Tk()
root.title("Band Name Generator")
root.geometry("300x180")

frame_city = ttk.Frame(root, padding=10)
frame_city.pack()
frame_pet = ttk.Frame(root, padding=10)
frame_pet.pack()
frame_button = ttk.Frame(root, padding=10)
frame_button.pack()

ttk.Label(frame_city, text="City where you grew up.").pack()
city_entry = ttk.Entry(frame_city)
city_entry.pack()

ttk.Label(frame_pet, text="Name of your childhood pet.").pack()
pet_entry = ttk.Entry(frame_pet)
pet_entry.pack()

ttk.Button(frame_button, text="Generate", command=generate_band_name).pack()

root.mainloop()
