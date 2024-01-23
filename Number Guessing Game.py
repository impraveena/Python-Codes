import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0

    while True:
        # Get user input for the guess
        user_guess = int(input("Enter your guess (between 1 and 100): "))
        
        # Increment the attempts count
        attempts += 1

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    number_guessing_game()

