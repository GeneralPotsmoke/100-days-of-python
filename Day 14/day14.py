import random

number_to_guess = random.randint(1, 100)
guess = None

while guess != number_to_guess:
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess < number_to_guess:
        print("Higher")
    elif guess > number_to_guess:
        print("Lower")
    else:
        print("Congratulations
