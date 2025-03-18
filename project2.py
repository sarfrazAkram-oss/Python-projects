import random
def guess_the_number():
    secret_number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I have picked a number between 1 and 100. Can you guess what it is?")

    while guess != secret_number:
        try:
            
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
