# =============================================================================
# NUMBER GUESSER
# Concepts: random numbers, while loops, if/elif/else, input validation,
#           type conversion, functions
# =============================================================================

import random


def get_difficulty():
    """Ask the player to choose a difficulty and return the upper bound."""
    print("Choose a difficulty:")
    print("  1 - Easy   (1 to 10)")
    print("  2 - Medium (1 to 50)")
    print("  3 - Hard   (1 to 100)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return 10
        elif choice == "2":
            return 50
        elif choice == "3":
            return 100
        else:
            print("That's not a valid option. Please enter 1, 2, or 3.")


def get_player_guess(upper_bound):
    """
    Ask the player for a guess and keep asking until they enter a valid number.
    Returns the guess as an integer.
    """
    while True:
        raw_input = input(f"Your guess (1-{upper_bound}): ").strip()

        # try/except catches the error if the player types something that
        # can't be converted to a number (e.g. "abc")
        try:
            guess = int(raw_input)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if guess < 1 or guess > upper_bound:
            print(f"Your guess must be between 1 and {upper_bound}.")
        else:
            return guess


def play_game():
    """Run one full round of the number guessing game."""
    upper_bound = get_difficulty()
    secret_number = random.randint(1, upper_bound)
    attempts = 0

    print(f"\nI've picked a number between 1 and {upper_bound}. Can you guess it?\n")

    while True:
        guess = get_player_guess(upper_bound)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try higher.\n")
        elif guess > secret_number:
            print("Too high! Try lower.\n")
        else:
            print(f"Correct! You got it in {attempts} attempt(s).")
            break


def main():
    print("=== Number Guesser ===\n")

    while True:
        play_game()

        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing!")
            break

        print()


if __name__ == "__main__":
    main()
