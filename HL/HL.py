import random

# Pick a random number between 1 and 50
secret_number = random.randint(1, 50)

print("Welcome to the number guesser game!")
print("I'm thinking of a number between 1 and 50.")
print("Take a guess!")

while True:
    # Get the user's guess
    user_guess = input("Enter a number: ")

    # Check if the user's guess is a valid number
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Check if the user's guess is within the range
    if user_guess < 1 or user_guess > 50:
        print("Invalid input. Please enter a number between 1 and 50.")
        continue

    # Check if the user's guess is correct
    if user_guess == secret_number:
        print(" Congratulations! You guessed the correct number!")
        break

    # Give a hint if the user's guess is too high or too low
    elif user_guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print("Too low! Try a higher number.")
