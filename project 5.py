import random
import string

def choose_word():
   
    words = ["python", "hangman", "programming", "developer", "computer", "keyboard"]
    return random.choice(words)

def display_board(word, guessed_letters):
  
    display = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word: " + " ".join(display))

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    
    while attempts > 0:
       
        display_board(word, guessed_letters)
        
    
        guess = input(f"\nYou have {attempts} attempts left. Guess a letter: ").lower()
        
       
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a valid single letter.")
            continue
        
    
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue
        
        guessed_letters.add(guess)
        
      
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word.")
        
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was: {word}")


hangman()
