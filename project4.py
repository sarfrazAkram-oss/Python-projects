import random

# Function 
def play_rps():
    #  choices
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    #  user input
    if user_choice not in choices:
        print("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")
        return 
    # Computer choice
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    #  winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")


play_rps()
