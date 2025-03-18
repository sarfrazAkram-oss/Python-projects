print("Welcome to Mad Libs!")
name = input("Enter a name: ")
# some inputs on our feelings -
adjective = input("Enter an adjective: ")
verb = input("Enter a verb (past tense): ")
noun = input("Enter a noun: ")
place = input("Enter a place: ")

story = (f"One day, {name} was feeling very {adjective}. They decided to {verb} to the {noun} at {place}.")

print("\nHere's your Mad Libs story:")
print(story)
