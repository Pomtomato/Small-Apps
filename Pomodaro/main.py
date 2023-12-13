import math
from tkinter import *

#---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    title_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print(f"repition = {reps}")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Relax", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        title_label.config(text = "Break", fg=PINK)
        count_down(short_break_sec)

    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    print(count_min, ":", count_sec)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.maxsize(width=400, height=400)
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato_jpg = PhotoImage(file="./Small-Apps/Pomodaro/tomato.png")
canvas.create_image(105,115, image = tomato_jpg)
timer_text = canvas.create_text(105,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(row=4, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=4, column=2)

check_marks = Label(text=" ",fg=GREEN, bg=YELLOW, font=(10))
check_marks.grid(row=5, column=1)


window.mainloop()