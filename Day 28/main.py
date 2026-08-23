import random

flashcards = {
    "Capital of Japan": "tokyo",
    "Largest planet": "jupiter",
    "Language this app is written in": "python",
    "8 bits make one": "byte",
    "Chemical symbol of Gold": "au"
}

"""The list of qustions/cards can be made dynamic by adding more flashcards to the dictionary using loops but I did't implement that here because I only wanted to test the logic."""
def start_quiz():
    questions = list(flashcards.keys())
    random.shuffle(questions)

    score = 0

    print("=" * 30)
    print("      FLASHCARD QUIZ")
    print("=" * 30)

    for question in questions:

        answer = input(f"\n{question}: ").lower().strip()

        if answer == flashcards[question]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Answer: {flashcards[question]}")

    percentage = (score / len(flashcards)) * 100

    print("\n" + "=" * 30)
    print("        RESULTS")
    print("=" * 30)
    print(f"Score      : {score}/{len(flashcards)}")
    print(f"Accuracy   : {percentage:.0f}%")

    if percentage == 100:
        print("Perfect!")
    elif percentage >= 60:
        print("Nice revision!")
    else:
        print("Time to study again.")


def add_flashcard():
    question = input("\nEnter new question: ")
    answer = input("Enter answer: ").lower()

    flashcards[question] = answer

    print("Flashcard added!")


def view_flashcards():
    print("\n------ FLASHCARDS ------")

    for question in flashcards:
        print(f"• {question}  →  {flashcards[question]}")


while True:

    print("""
==============================
1. Start Quiz
2. Add Flashcard
3. View Flashcards
4. Exit
==============================
""")

    choice = input("Choose: ")

    if choice == "1":
        start_quiz()

    elif choice == "2":
        add_flashcard()

    elif choice == "3":
        view_flashcards()

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("Invalid option.")