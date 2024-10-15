# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import messagebox

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
rep = 0
timer = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer, rep
    canva.after_cancel(timer)
    canva.itemconfig(timer_lable, text="00:00")
    lable.config(text='Timer')
    check_mark.config(text='')
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global rep
    rep += 1
    if rep % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        lable.config(text='BREAK', fg=RED)
        messagebox.showinfo("information", "you have completed the 4 cycles work sessions")
        rep = 0
    elif rep % 2 == 1:
        count_down(WORK_MIN*60)
        lable.config(text='WORK', fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN*60)
        lable.config(text='BRAKE', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(n):
    global timer
    minute = n // 60
    seconds = n % 60
    if seconds < 10:
        seconds = f'0{seconds}'
    canva.itemconfig(timer_lable, text=f'{minute}:{seconds}')
    if n > 0:
        timer = canva.after(1000, count_down, n - 1)
    else:
        start()
        markc = rep // 2
        check_mark.config(text="✔" * markc)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.geometry("450x450")
window.title('Pomodor_Game')
window.config(padx=50, pady=50, bg=YELLOW)
lable = Label(text='TIMER', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, 'bold'))
lable.grid(column=1, row=0)

canva = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_path = PhotoImage(file='tomato.png')
canva.create_image(100, 112, image=image_path)
timer_lable = canva.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='white')
canva.grid(column=1, row=1)

start_button = Button(text='start', font=FONT_NAME, highlightthickness=0, command=start)
start_button.grid(column=0, row=2)
reset_button = Button(text='reset', font=FONT_NAME, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)
check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, 'bold'))
check_mark.grid(column=1, row=3)
window.mainloop()
