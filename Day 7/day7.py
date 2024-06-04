word = "python"
guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("
You Win!")
        break

    guess = input("
Guess a letter: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong!")
        print(f"You have {turns} more guesses")
        if turns == 0:
            print("You Lose!")
