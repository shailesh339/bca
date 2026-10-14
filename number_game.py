import random

def play_game():
    print("========================================")
    print("      WELCOME TO GUESS THE NUMBER!      ")
    print("========================================")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it within 7 attempts?\n")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("Too high! Try a lower number.\n")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break
    else:
        print(f"❌ Game Over! The secret number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    while True:
        play_game()
        replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if replay not in ['y', 'yes']:
            print("Thanks for playing! Goodbye!")
            break
        print("\n" + "="*40 + "\n")