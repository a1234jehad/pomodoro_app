import tkinter
import math


def raise_above_all(w):
    w.attributes('-topmost', 1)
    w.attributes('-topmost', 0)


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None
runing = False


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text="")
    global reps
    reps = 0
    global runing
    runing = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global runing

    if runing:
        pass
    else:
        reps += 1
        runing = True
        if reps % 2 == 0:
            # SHORT_BREAK_MIN
            count_down(SHORT_BREAK_MIN)
            timer_label.config(text="Break", fg=RED)
        elif reps % 8 == 0:
            count_down(LONG_BREAK_MIN)
            timer_label.config(text="Break", fg=PINK)
        else:
            # WORK_MIN
            count_down(WORK_MIN)
            timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(cnt):
    global runing
    runing = True
    min = math.floor(cnt / 60)
    sec = cnt % 60
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if cnt > 0:
        global timer
        timer = window.after(1000, count_down, cnt - 1)
    else:
        runing = False
        start_timer()
        marks = ""
        works_done = math.floor(reps / 2)
        for x in range(works_done):
            marks += '\u2713'
        check_marks.config(text=marks)
        raise_above_all(window)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# image
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image, )
timer_text = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill='white')
canvas.grid(column=2, row=2)

# labels
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)
check_marks = tkinter.Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_marks.grid(column=2, row=4)

# buttons
start_button = tkinter.Button(text=' Start ', font=(FONT_NAME, 12), highlightthickness=0, command=start_timer,
                              relief='groove', bg=GREEN)
reset_button = tkinter.Button(text='Restart', font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=timer_reset,
                              relief='groove', bg=GREEN, fg=RED)
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)

window.mainloop()
