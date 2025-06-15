import random
# Show the game introduction
def show_intro():
    print("="*50)
    print("Welcome to Hack the Vault - A Cybersecurity Minitgame!")
    print("="*50)
    print("You are a hacker trying to break into a secure digital vault.")
    print("The system has generated a secret 4-digit code.")
    print("Your job is the guess the code before you run out of attempts.")
    print("Instructions:")
    print("Enter a 4-digit number (digits only).")
    print(" - You'll get feedback after each guess:")
    print(" - How many digits are correct but in the wrong position.")
    print(" - How many digits are correct and in the correct position.")
    print("- You have 6 attempts to guess the code.")

# Get difficulty level from the user ( sets password length)
def get_difficulty():
    while True:
        level = input("Choose difficulty Easy(3), Medium(4), Hard(6): ").strip().lower()
        if level in ["3", "easy"]:
            return 3
        elif level in ["4", "medium"]:
            return 4
        elif level in ["6", "hard"]:
            return 6
        else:
            print("Invalid choice. Please choose 3, 4, or 6.")

# Generate a random 4-digit code
def generate_password(length=4):
    digits = "0123456789"
    return ''.join(random.choices(digits, k=length))

#Compare guess with password and provide feedback
def check_guess(password, guess):
    correct_position = sum((p == g) for p, g in zip(password, guess))
    correct_chars = sum(min(password.count(d), guess.count(d)) for d in set(guess))
    return correct_chars, correct_position

#Main gane loop
def play_game():
    show_intro()
    length = get_difficulty()
    password = generate_password(length)
    attempts = 6

    while attempts > 0:
        guess = input(f"Enter your {length}-digit guess: ")

        if len(guess) != length or not guess.isdigit():
            print(f"Invalid input. Please enter digits only with the correct length.")
            continue

        correct_chars, correct_position = check_guess(password, guess)
        print(f"Correct digits (any position): {correct_chars}")
        print(f"Correct digits in correct position: {correct_position}")

        if guess == password:
            print("Congratulations! You hacked the vault!")
            break
        else:
            attempts -= 1
            print(f"Attempts remaining: {attempts}")

        if attempts == 0:
            print(f"Game Over! The correct code was: {password}")



# Run the game
def main():
    while True:
        play_game()
        again = input("Would you like to play again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing Hack the Vault!")
            break



# Function to check the guess against the password
        def check_guess(password, guess):
            correct_position = sum(p == g for p, g in zip(password, guess))
            # Count digits in both password and guess
            from collections import Counter
            password_counter = Counter(password)
            guess_counter = Counter(guess)
            # Count correct digits regardless of position
            correct_chars = sum((password_counter & guess_counter).values())
            # Subtract those already counted as correct position
            correct_chars -= correct_position
            return correct_chars, correct_position

    # Start the game
if __name__ == "__main__":
    main()


        