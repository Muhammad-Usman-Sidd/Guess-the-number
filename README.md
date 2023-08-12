# Random Number Guessing Game
## Introduction
This is a simple Python program that implements a random number guessing game. The program generates a random two-digit number, and the user's task is to guess that number within the fewest attempts possible.
## How to Play

1. Run the Python script `random_number_game.py`.
2. The program will generate a random number between 0 and 99 (inclusive).
3. The user will be prompted to input their guess of the generated number.
4. If the input is not an integer, the program will ask for a valid input.
5. If the guessed number is correct, the user wins the game.
6. If the guessed number is incorrect, the program provides hints ("larger" or "smaller") to guide the user towards the correct answer.
7. The game continues until the user guesses the correct number.
8. After successfully guessing the number, the program displays the number of attempts it took to win.

## Highscore

The game keeps track of the best score (fewest number of attempts) and displays a message if the user breaks the previous highscore.

The highscore is saved in the `highscore.txt` file. If the file does not exist or if the current user's score is better than the previous highscore, the program updates the highscore.

## Difficulty Levels

The game provides feedback based on the number of attempts taken by the user:
- If the user guesses the number within 5 attempts, they are called a genius!
- If the user guesses the number within 10 attempts, they are told "Not bad!"
- If the user takes more than 10 attempts, they are encouraged to try again next time.

## Usage

1. Clone the repository or download the `random_number_game.py` file.
2. Make sure you have Python installed on your machine.
3. Open a terminal or command prompt and navigate to the directory where the `random_number_game.py` file is located.
4. Run the script using the command: `python random_number_game.py`.

## Contact

For inquiries, questions, or feedback, please contact [Muhammad Usman] at [usman.the.coder@gmail.com].
