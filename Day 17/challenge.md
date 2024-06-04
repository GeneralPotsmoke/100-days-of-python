#### Day 17: The Quiz Project & the Benefits of OOP
**Challenge:** Create a quiz application using OOP, where the questions and answers are stored in objects.

```python
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_number = 0

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}
")

question_bank = [
    Question("The sky is blue.", "True"),
    Question("The grass is green.", "True"),
    Question("Python is a type of snake.", "True"),
]

quiz = Quiz(question_bank)
while quiz.question_number < len(question_bank):
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
```


