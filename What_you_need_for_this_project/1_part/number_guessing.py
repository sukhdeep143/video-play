import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    lower = 1
    upper = 100
    number_to_guess = random.randint(lower, upper)
    attempts = 0

    print(f"I'm thinking of a number between {lower} and {upper}.")

    while True:
        try:
            guess = int(input("🔢 Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 Too low! Try again.")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.")
            else:
                print(f"✅ Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

number_guessing_game()
