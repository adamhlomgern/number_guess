# Random number game


# Imports
import random
from art import logo


# Global Variables
number_of_guesses = 0
target_number = 0

# Functions
def start_game():
    global target_number
    print(logo)
    print("Welcome to the random number game!")
    target_number = random.randint(1, 100)
    difficulty()
    guess_loop()

def difficulty():
    global number_of_guesses
    difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_choice == "easy":
        number_of_guesses = 10
    elif difficulty_choice == "hard":
        number_of_guesses = 5
    else:
        print("Please return a valid answer.")
        difficulty()

def guess_loop():
    global number_of_guesses
    while number_of_guesses > 0:
        player_guess = int(input("Enter your guess(1-100): "))
        print(f"Your guess is: {player_guess}")
        if player_guess > target_number:
            print("Too high.")
        elif player_guess < target_number:
            print("Too low.")
        else:
            print(f"Correct! The number was {target_number}.")
            replay()
            return
        number_of_guesses -= 1
        print(f"You have {number_of_guesses} guesses left.")
        replay()

def replay():
    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again == "yes":
        start_game()
    else:
        print("Thank you for playing!")