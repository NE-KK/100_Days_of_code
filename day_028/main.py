from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count -1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer",
              font=(FONT_NAME, 50),
              fg=GREEN,
              bg=YELLOW)
label.grid(row=0, column=1)

button_start = Button(text="Start")
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset")
button_reset.grid(row=2, column=2)

label_check = Label(text="✔",
                    font=(FONT_NAME, 15, "bold"),
                    fg=GREEN,
                    bg=YELLOW)
label_check.grid(row=3, column=1)

canvas = Canvas(height=230,  width=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(112, 112, image=tomato_img)
timer_text = canvas.create_text(112, 130, fill="white", font=(FONT_NAME, 35, "bold"), text="00:00")
canvas.grid(row=1, column=1)

count_down(5)
window.mainloop()
