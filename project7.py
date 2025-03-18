import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the pool of characters (uppercase, lowercase, digits, punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password by picking 'length' number of random characters from the pool
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Ask the user for the number of passwords and their length
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        password_length = int(input("Enter the desired length of each password: "))
        
        if num_passwords <= 0 or password_length <= 0:
            print("Please enter positive values for the number of passwords and length.")
        else:
            # Generate and display the passwords
            print("\nGenerated Passwords:")
            for i in range(num_passwords):
                password = generate_password(password_length)
                print(f"Password {i + 1}: {password}")
    
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Run the program
main()
