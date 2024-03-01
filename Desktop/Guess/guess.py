import random

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def evaluate_guess(secret_number, user_guess):
    if user_guess == secret_number:
        return "Congratulations! You guessed the correct number."
    elif user_guess < secret_number:
        return "Too low! Try a higher number."
    else:
        return "Too high! Try a lower number."

def play_guess_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = generate_random_number()

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        user_guess = get_user_guess()
        attempts += 1

        result = evaluate_guess(secret_number, user_guess)
        print(result)

        if user_guess == secret_number:
            print(f"You guessed the number in {attempts} attempts!")
            break

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    play_guess_game()
