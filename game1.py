import random

# Define the possible options
options = ["rock", "paper", "scissors"]

# Get user's choice
user_choice = input("Rock, paper, or scissors? ").lower()

# Check if the user's choice is valid
if user_choice not in options:
    print("Invalid choice. Please enter rock, paper, or scissors.")
else:
    # Get the computer's choice
    computer_choice = random.choice(options)

    # Compare the choices and determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors.")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock.")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors beats paper.")
    else:
        print(f"You lose! {computer_choice.capitalize()} beats {user_choice}.")