# =============================================================================
# QUIZ GAME
# Concepts: lists, dictionaries, for loops, functions, f-strings,
#           score tracking, random.shuffle
# =============================================================================

import random


# A list of dictionaries — each dictionary holds one question.
# This is a great pattern: related data grouped together.
QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B",
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["A) 5", "B) 7", "C) 8", "D) 6"],
        "answer": "D",
    },
    {
        "question": "What is 12 multiplied by 12?",
        "options": ["A) 124", "B) 144", "C) 132", "D) 148"],
        "answer": "B",
    },
    {
        "question": "Which language is Python named after?",
        "options": ["A) A snake", "B) Monty Python", "C) A Greek god", "D) A scientist"],
        "answer": "B",
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A) Central Processing Unit",
            "B) Computer Personal Unit",
            "C) Central Program Utility",
            "D) Core Processing Unit",
        ],
        "answer": "A",
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A) O2", "B) CO2", "C) H2O", "D) HO"],
        "answer": "C",
    },
    {
        "question": "In binary, what is the value of 1010?",
        "options": ["A) 8", "B) 9", "C) 10", "D) 12"],
        "answer": "C",
    },
]

VALID_ANSWERS = {"A", "B", "C", "D"}


def ask_question(question_data, question_number):
    """
    Display a single question and return True if the player answered correctly.
    """
    print(f"Question {question_number}: {question_data['question']}")

    for option in question_data["options"]:
        print(f"  {option}")

    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in VALID_ANSWERS:
            break
        print("Please enter A, B, C, or D.")

    if answer == question_data["answer"]:
        print("Correct!\n")
        return True
    else:
        correct_letter = question_data["answer"]
        # Find the full text of the correct option to show the player
        correct_option = next(
            opt for opt in question_data["options"] if opt.startswith(correct_letter)
        )
        print(f"Wrong. The correct answer was {correct_option}\n")
        return False


def show_results(score, total):
    """Print the final score and a message based on how well the player did."""
    percentage = (score / total) * 100
    print("=" * 40)
    print(f"Quiz over! You scored {score} out of {total} ({percentage:.0f}%)")

    if percentage == 100:
        print("Perfect score! Outstanding!")
    elif percentage >= 75:
        print("Great work!")
    elif percentage >= 50:
        print("Not bad — keep practising!")
    else:
        print("Better luck next time!")

    print("=" * 40)


def main():
    print("=== Quiz Game ===\n")

    # Shuffle a copy of the questions so the order is different each time
    questions = QUESTIONS.copy()
    random.shuffle(questions)

    score = 0

    for index, question_data in enumerate(questions, start=1):
        is_correct = ask_question(question_data, index)
        if is_correct:
            score += 1

    show_results(score, len(questions))


if __name__ == "__main__":
    main()
