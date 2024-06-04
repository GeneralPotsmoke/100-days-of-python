#### Day 27: Tkinter, *args, **kwargs and Creating GUI Programs
**Challenge:** Create a simple Tkinter GUI program with a button and a label, using *args and **kwargs.

```python
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
```


