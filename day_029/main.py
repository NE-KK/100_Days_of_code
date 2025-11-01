from tkinter import *
from random import randint

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
char_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z",
             "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z",
             "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
             "!", "$", "%", "&", "(", ")", "=", "?", "/", "#", "+", "-", "*", "@", "[", "]", "{", "}", "~", ";", ":"]
password_list = []

def generate_password():
    entry_password.delete(0, END)
    for i in range(10):
        list_num = randint(0, len(char_list) - 1)
        password_list.append(char_list[list_num])


    password_str = ''.join(password_list)
    entry_password.insert(0, password_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(pady=20, padx=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# label website -----------------------
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
# entry website -----------------------
entry_website = Entry(width=42)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2)

# label email -------------------------
label_email = Label(text="E-Mail/Username:")
label_email.grid(row=2, column=0)
# entry email -------------------------
entry_email = Entry(width=42)
entry_email.insert(0, "myname@gmail.com")
entry_email.grid(row=2, column=1, columnspan=2)

# label password ----------------------
label_password = Label(text="Password")
label_password.grid(row=3, column=0)
# entry password ----------------------
entry_password = Entry(window, width=32)
entry_password.grid(row=3, column=1)
# button password ---------------------
button_password = Button(text="Generate", command=generate_password)
button_password.grid(row=3, column=2)

# button add --------------------------
button_add = Button(text="Add", width=36)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
