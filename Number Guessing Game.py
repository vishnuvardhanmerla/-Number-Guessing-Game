import random

def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))

    secret_number = random.randint(lower, upper)
    attempts = 0
    max_attempts = 5

    print(f"\nI have selected a number between {lower} and {upper}. You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! 📉")
            elif guess > secret_number:
                print("Too high! 📈")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

    else:
        print(f"❌ Sorry! You've used all attempts. The number was: {secret_number}")

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
