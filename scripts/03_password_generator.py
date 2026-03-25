# =============================================================================
# PASSWORD GENERATOR
# Concepts: string module, random, list comprehensions, join,
#           functions, input validation, boolean flags
# =============================================================================

import random
import string


def get_positive_integer(prompt):
    """Keep asking until the user gives us a whole number greater than zero."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("That's not a valid number. Try again.")


def ask_yes_no(prompt):
    """Ask a yes/no question and return True for yes, False for no."""
    while True:
        answer = input(prompt + " (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please type yes or no.")


def build_character_pool(use_uppercase, use_digits, use_symbols):
    """
    Build the set of characters to pick from based on the user's choices.
    Always includes lowercase letters as a baseline.
    """
    pool = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

    if use_uppercase:
        pool += string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if use_digits:
        pool += string.digits  # '0123456789'

    if use_symbols:
        pool += string.punctuation  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    return pool


def generate_password(length, character_pool):
    """
    Generate a random password of the given length using the character pool.

    List comprehension builds a list of random characters, then join
    combines them all into one string.
    """
    characters = [random.choice(character_pool) for _ in range(length)]
    return "".join(characters)


def assess_strength(length, use_uppercase, use_digits, use_symbols):
    """Return a simple strength label based on length and character variety."""
    variety_score = sum([use_uppercase, use_digits, use_symbols])

    if length >= 16 and variety_score == 3:
        return "Strong"
    elif length >= 12 and variety_score >= 2:
        return "Good"
    elif length >= 8:
        return "Fair"
    else:
        return "Weak"


def main():
    print("=== Password Generator ===\n")

    length = get_positive_integer("How long should the password be? ")
    use_uppercase = ask_yes_no("Include uppercase letters?")
    use_digits = ask_yes_no("Include numbers?")
    use_symbols = ask_yes_no("Include symbols?")

    character_pool = build_character_pool(use_uppercase, use_digits, use_symbols)

    how_many = get_positive_integer("\nHow many passwords would you like to generate? ")

    print(f"\n--- Generated Passwords ---")
    for i in range(how_many):
        password = generate_password(length, character_pool)
        strength = assess_strength(length, use_uppercase, use_digits, use_symbols)
        print(f"  {i + 1}. {password}  [{strength}]")

    print()
    print(f"Character pool size: {len(character_pool)} characters")
    print(f"Possible combinations: {len(character_pool) ** length:,}")


if __name__ == "__main__":
    main()
