import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FG = GREEN
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def Reset():
    global REPS
    REPS = 0

    canvas.itemconfig(timer_text, text="00:00")
    timer_word.config(text="Timer")
    tick_mark.config(text="")
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def Start():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_word.config(text="Long Break!", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_word.config(text="Short Break!", fg=PINK)
    else:
        timer_word.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global REPS

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = (f"0{count_sec}")

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        Start()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✓"
        tick_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(115, 130, text="00:00", fill="aliceblue",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


timer_word = tkinter.Label(text="Timer", font=(
    "Arial", 24, "bold"), foreground=FG, bg=YELLOW)
timer_word.grid(row=0, column=1)

tick_mark = tkinter.Label(font=(
    "Arial", 24, "bold"), foreground=FG, bg=YELLOW)
tick_mark.grid(row=3, column=1)

start_button = tkinter.Button(text="Start", command=Start)
start_button.config(padx=3, pady=3)
start_button.grid(row=2, column=0)


Reset_button = tkinter.Button(text="Reset", command=Reset)
Reset_button.config(padx=3, pady=3)
Reset_button.grid(row=2, column=2)


window.mainloop()