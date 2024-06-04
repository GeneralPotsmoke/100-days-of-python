#### Day 89: Portfolio Project - Disappearing Text Writing App
**Challenge:** Create a Tkinter application where the text disappears if the user stops typing for more than 5 seconds.

```python
import tkinter as tk
from tkinter import messagebox
import time

class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text Writing App")
        self.textbox = tk.Text(root, font=('Arial', 14), width=50, height=15)
        self.textbox.pack(pady=10)
        self.last_type_time = time.time()
        self.textbox.bind('<Key>', self.reset_timer)
        self.check_disappearance()

    def reset_timer(self, event):
        self.last_type_time = time.time()

    def check_disappearance(self):
        current_time = time.time()
        if current_time - self.last_type_time > 5:
            self.textbox.delete('1.0', tk.END)
        self.root.after(1000, self.check_disappearance)

root = tk.Tk()
app = DisappearingTextApp(root)
root.mainloop()
```


