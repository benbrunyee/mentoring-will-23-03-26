# =============================================================================
# FILE CREATOR
# Concepts: os module, file writing with open(), for loops, random,
#           f-strings, string formatting, creating directories
# =============================================================================
#
# This script creates a folder called "sample_files/" full of random .txt files.
# Run this first, then use 05_file_searcher.py to search through them.
# =============================================================================

import os
import random

OUTPUT_FOLDER = "sample_files"

ANIMALS = ["cat", "dog", "fox", "bear", "wolf", "eagle", "shark", "tiger", "rabbit", "owl"]
COLOURS = ["red", "blue", "green", "yellow", "purple", "orange", "silver", "golden"]
VERBS = ["runs", "jumps", "flies", "swims", "sleeps", "hunts", "hides", "climbs"]
PLACES = ["in the forest", "near the river", "on the mountain", "by the sea", "in the city"]

# A small pool of facts we can sprinkle into files so there's something to search for
FACTS = [
    "Python was created by Guido van Rossum.",
    "The Earth orbits the Sun once every 365.25 days.",
    "Water boils at 100 degrees Celsius at sea level.",
    "The speed of light is approximately 299,792 km/s.",
    "A byte consists of 8 bits.",
    "Shakespeare wrote 37 plays.",
    "The Great Wall of China is over 13,000 miles long.",
    "Mount Everest is 8,849 metres tall.",
]


def generate_sentence():
    """Build a random sentence from our word lists."""
    animal = random.choice(ANIMALS)
    colour = random.choice(COLOURS)
    verb = random.choice(VERBS)
    place = random.choice(PLACES)
    return f"The {colour} {animal} {verb} {place}."


def generate_file_content(file_number):
    """
    Generate the text content for one file.
    Each file gets a heading, some random sentences, and occasionally a fact.
    """
    lines = []
    lines.append(f"File #{file_number}")
    lines.append("=" * 30)
    lines.append("")

    sentence_count = random.randint(3, 8)
    for _ in range(sentence_count):
        lines.append(generate_sentence())

    # Roughly half the files will contain a fact
    if random.random() > 0.5:
        lines.append("")
        lines.append("Did you know?")
        lines.append(random.choice(FACTS))

    return "\n".join(lines)


def create_sample_files(count):
    """Create `count` text files inside the OUTPUT_FOLDER directory."""

    # os.makedirs creates the folder (and any parent folders) if it doesn't exist.
    # exist_ok=True means it won't crash if the folder is already there.
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for i in range(1, count + 1):
        filename = f"file_{i:03d}.txt"  # e.g. file_001.txt, file_042.txt
        filepath = os.path.join(OUTPUT_FOLDER, filename)

        content = generate_file_content(i)

        # open() with "w" mode creates the file if it doesn't exist, or
        # overwrites it if it does. The 'with' statement automatically
        # closes the file when we're done, even if an error occurs.
        with open(filepath, "w") as file:
            file.write(content)

    print(f"Created {count} files in '{OUTPUT_FOLDER}/'")


def main():
    print("=== File Creator ===\n")

    print("This script will create a folder of random text files.")
    print("You can then search through them using 05_file_searcher.py\n")

    while True:
        raw = input("How many files should I create? (1-200): ").strip()
        try:
            count = int(raw)
            if 1 <= count <= 200:
                break
            else:
                print("Please enter a number between 1 and 200.")
        except ValueError:
            print("That's not a valid number.")

    create_sample_files(count)

    print(f"\nDone! Open the '{OUTPUT_FOLDER}' folder to see the files.")
    print("Now run 05_file_searcher.py to search through them.")


if __name__ == "__main__":
    main()
