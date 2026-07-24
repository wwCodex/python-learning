import random

word_list = [
    "python", "apple", "computer", "guitar", "ocean",
    "planet", "rocket", "school", "hangman", "friend"
]

stages = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]


def choose_word():
    return random.choice(word_list)


def display_word(word, guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


def play_game():

    word = choose_word()

    guessed_letters = []

    lives = 6

    print("\nWelcome to Hangman!\n")

    while lives > 0:

        print(stages[6 - lives])

        print(f"Lives Left: {lives}")

        display_word(word, guessed_letters)

        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter only ONE letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Wrong!")
            lives -= 1

        if is_word_guessed(word, guessed_letters):
            print("\n🎉 Congratulations!")
            print(f"The word was: {word}")
            return

    print(stages[6])

    print("\nGame Over!")
    print(f"The word was: {word}")


while True:

    play_game()

    again = input("\nPlay Again? (y/n): ").lower()

    if again != "y":
        print("\nThanks for playing!")
        break