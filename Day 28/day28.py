import tkinter as tk
import time

def start_timer():
    global running
    running = True
    countdown(25 * 60)

def stop_timer():
    global running
    running = False

def reset_timer():
    global running
    running = False
    canvas.itemconfig(timer_text, text="00:00")

def countdown(count):
    if running:
        minutes = count // 60
        seconds = count % 60
        canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
        if count > 0:
            window.after(1000, countdown, count - 1)

window = tk.Tk()
window.title("Pomodoro Timer")

canvas = tk.Canvas(window, width=200, height=224, bg="yellow")
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=("Arial", 35, "bold"))
canvas.pack()

start_button = tk.Button(window, text="Start", command=start_timer)
start_button.pack(side="left")

stop_button = tk.Button(window, text="Stop", command=stop_timer)
stop_button.pack(side="left")

reset_button = tk.Button(window, text="Reset", command=reset_timer)
reset_button.pack(side="right")

running = False

window.mainloop()
