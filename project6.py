import time

def countdown_timer(seconds):
    while seconds > 0:
        
        print(f"Time remaining: {seconds} seconds", end="\r")
        time.sleep(1)
        seconds -= 1  

    print("Time's up!")  


try:
    user_input = int(input("Enter the time in seconds for the countdown: "))
    if user_input <= 0:
        print("Please enter a positive number for the countdown.")
    else:
        countdown_timer(user_input)
except ValueError:
    print("Please enter a valid integer for the countdown.")
