import random
import os

random_number = random.randint(0, 99)
user_guess = None
guesses = 0
print("\t\t\t\tHINT: It's a two digit number!!\n")
while user_guess != random_number:
    try:
        user_guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    if user_guess == random_number:
        print("You guessed it right!")
    else:
        print("You guessed it wrong!")
        if user_guess > random_number:
            print("Enter a smaller number.")
        else:
            print("Enter a larger number.")
        guesses += 1

print(f"You guessed it in {guesses} tries.")

highscore = float('inf')
if os.path.exists("highscore.txt"):
    try:
        with open("highscore.txt", "r") as f:
            highscore_value = f.read().strip()
            if len(highscore_value) > 0:
                highscore = int(highscore_value)
    except ValueError:
        pass

if guesses < highscore:
    print("You have just broken the highscore!")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses)+"guesses is currently the the highscore ")

if guesses <= 5:
    print("You are a genius!")
elif guesses <= 10:
    print("Not bad!")
else:
    print("Better luck next time.")
