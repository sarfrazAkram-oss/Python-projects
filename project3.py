import random

# Function 
def computer_guess():
    print("Welcome to 'Guess the Number' where the computer guesses your number!")
    print("Think of a number between 1 and 100 and I'll try to guess it.")

    #  initial range
    low = 1
    high = 100
    feedback = ""

    while feedback != "correct":

        guess = random.randint(low, high)
        print(f"My guess is: {guess}")
 
        feedback = input("Is my guess too high, too low, or correct? ").lower()
       
        if feedback == "too high":
            high = guess - 1
        elif feedback == "too low":
            low = guess + 1
        elif feedback != "correct":
            print("Please respond with 'too high', 'too low', or 'correct'.")

    print(f"Yay! I guessed your number {guess} correctly!")

computer_guess()
