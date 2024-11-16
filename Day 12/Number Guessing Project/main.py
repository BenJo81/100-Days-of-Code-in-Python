import random
from art import logo
turns = 0
guess = 0

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
chosen_number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    turns = 10
else:
    turns = 5

while turns > 0:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns -= 1
    if guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}.")
        turns = 0
    elif guess > chosen_number:
        print("Too high.\nGuess again.")
    elif guess < chosen_number:
        print("Too low.\nGuess again.")