from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECONDS = 0
interval = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text='Timer', bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text='')
    global interval
    interval = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():

    global interval
    interval += 1

    if interval % 8 == 0:
        timer_label.config(text='Long Break!!', fg=RED)
        count_down(LONG_BREAK_MIN, SECONDS)
    elif interval % 2 == 0:
        timer_label.config(text='Short Break!!', fg=PINK)
        count_down(SHORT_BREAK_MIN, SECONDS)
    else:
        timer_label.config(text='Work Work Work!!', fg=GREEN)
        count_down(WORK_MIN, SECONDS)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(minutes, seconds):
    if minutes >= 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
        if seconds == 0:
            minutes -= 1
            seconds = 59
            timer = window.after(1000, count_down, minutes, seconds)
        else:
            timer = window.after(1000, count_down, minutes, seconds-1)
    else:
        start_timer()
        marks = ""
        work_sessions = interval//2
        for _ in range(work_sessions):
            marks += "✓"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'bold'))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 20, 'bold'), fill='white')
canvas.grid(column=1, row=1)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, 'bold'))
check_label.grid(column=1, row=3)

window.mainloop()
