import tkinter as tk

def button_clicked(*args, **kwargs):
    label.config(text="Button Clicked!")

window = tk.Tk()
window.title("Tkinter GUI")

label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

button = tk.Button(window, text="Click Me", command=lambda: button_clicked())
button.pack()

window.mainloop()
