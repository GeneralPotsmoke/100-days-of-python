import tkinter as tk
from tkinter import messagebox
import time

sample_text = "The quick brown fox jumps over the lazy dog."

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.text_label = tk.Label(root, text=sample_text, font=('Arial', 14))
        self.text_label.pack(pady=10)
        self.entry = tk.Entry(root, font=('Arial', 14), width=50)
        self.entry.pack(pady=10)
        self.start_button = tk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack(pady=5)
        self.result_label = tk.Label(root, text="", font=('Arial', 14))
        self.result_label.pack(pady=10)
        self.start_time = None

    def start_test(self):
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.start_time = time.time()
        self.entry.bind('<Return>', self.calculate_speed)

    def calculate_speed(self, event):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        typed_text = self.entry.get()
       

 words_per_minute = len(typed_text.split()) / (elapsed_time / 60)
        accuracy = sum(1 for a, b in zip(typed_text, sample_text) if a == b) / len(sample_text) * 100
        self.result_label.config(text=f"Speed: {words_per_minute:.2f} WPM
Accuracy: {accuracy:.2f}%")

root = tk.Tk()
app = TypingSpeedTest(root)
root.mainloop()
