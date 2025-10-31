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
reps = 0
timer_id = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    label.config(text="Timer", font=(FONT_NAME, 50), fg=GREEN)
    label_check.config(text="")
    # window.after_cancel(timer_id)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
        text = label_check["text"]
        label_check.config(text=text + "✔")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
        text = label_check["text"]
        label_check.config(text=text + "✔")
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if count_min < 10:
        count_min_str = "0" + str(count_min)
    else:
        count_min_str = str(count_min)

    if count_sec < 10:
        count_sec_str = "0" + str(count_sec)
    else:
        count_sec_str = str(count_sec)

    count_text = count_min_str + ":" + count_sec_str

    canvas.itemconfig(timer_text, text=count_text)
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

button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=reset)
button_reset.grid(row=2, column=2)

label_check = Label(text="",
                    font=(FONT_NAME, 15, "bold"),
                    fg=GREEN,
                    bg=YELLOW)
label_check.grid(row=3, column=1)

canvas = Canvas(height=230,  width=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(112, 112, image=tomato_img)
timer_text = canvas.create_text(112, 130, fill="white", font=(FONT_NAME, 35, "bold"), text="00:00")
canvas.grid(row=1, column=1)

window.mainloop()
