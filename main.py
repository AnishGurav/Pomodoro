from tkinter import *
import math
from plyer import notification
# ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
pink = "#fe91ae"
FONT_NAME = "Courier"
white_pink = "#eec4c4"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(timer_heading, text="TIMER\n   ⏲️")
    global REPS
    REPS = 0
    start_button.config(text="Start", font=("Helvetica", 20, "bold"), command=start_timer)

def stop_timer():
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    # count_down(5*60)
    start_button.config(text="Stop",font=("Helvetica", 20, "bold"),command=stop_timer)
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        canvas.itemconfig(timer_heading, text = "LONG\nBREAK")
        notification.notify(
            title="WELL DONE",
            message="Now Relax for a while",
            timeout=10
        )
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        canvas.itemconfig(timer_heading, text="SHORT\nBREAK")
        notification.notify(
            title="GOOD JOB",
            message="Time to take a short break",
            timeout=10
        )
    else:
        count_down(work_sec)
        canvas.itemconfig(timer_heading, text="WORK\nTIME 🕮", fill="black")
        notification.notify(
            title="HEY!!",
            message="Start Working",
            timeout=10
        )

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    # if count_sec == 0:
    #     count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Promodoro Timer")
window.config(bg=pink)

canvas = Canvas(width=500, height=400, highlightthickness=0)
anime_img = PhotoImage(file="image.png")
canvas.create_image(200, 200, image=anime_img)
timer_text = canvas.create_text(100, 200, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
timer_heading = canvas.create_text(100, 100, text="TIMER\n   ⏲️", fill="black", font=("Helvetica", 40, "bold"))
canvas.grid(column=4, row=2)

# current_task = Label(text="hello", fg="black", font=("Helvetica", 40, "bold"))
# current_task.grid(column=4, row=3)
# timer = Label(text="TIMER", font=(FONT_NAME, 40, "bold"))
# timer.grid(column=1, row=0)

space = Label(text="...", fg=pink, bg=pink, font=(10))
space.grid(column=0, row=0)
space1 = Label(text="..", fg=pink, bg=pink, font=(10))
space1.grid(column=2, row=0)

start_button = Button(text="Start", command=start_timer, fg="white", bg="black")
start_button.config(font=("Helvetica", 20, "bold"))
start_button.grid(column=1, row=1)

# stop_button = Button(text="Start", command=start_timer, fg="white", bg="black")
# stop_button.config(font=("Helvetica", 20, "bold"))
# stop_button.grid(column=1, row=1)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(font=("Helvetica", 20, "bold"))
reset_button.grid(column=3, row=1)

window.mainloop()