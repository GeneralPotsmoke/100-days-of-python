import requests
import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz App")

        self.question_text = tk.StringVar()
        self.label = tk.Label(self.window, textvariable=self.question_text, wraplength=400)
        self.label.pack(pady=20)

        self.true_button = tk.Button(self.window, text="True", command=lambda: self.check_answer("True"))
        self.true_button.pack(side="left", padx=20)

        self.false_button = tk.Button(self.window, text="False", command=lambda: self.check_answer("False"))
        self.false_button.pack(side="right", padx=20)

        self.score = 0
        self.get_question()

        self.window.mainloop()

    def get_question(self):
        response = requests.get("https://opentdb.com/api.php?amount=1&type=boolean")
        response.raise_for_status()
        data = response.json()
        self.question_data = data["results"][0]
        self.question_text.set(self.question_data["question"])

    def check_answer(self, answer):
        if answer == self.question_data["correct_answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", f"Your score: {self.score}")
        else:
            messagebox.showinfo("Incorrect", f"Your score: {self.score}")
        self.get_question()

quiz_app = QuizApp()
