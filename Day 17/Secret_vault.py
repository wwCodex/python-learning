import random


def generate_code():
    code = []

    for i in range(3):
        code.append(random.randint(0, 9))

    return code


def get_guess():
    guess = input("\nEnter a 3-digit code: ")

    if len(guess) != 3 or not guess.isdigit():
        print("Enter exactly 3 numbers!")
        return None

    return [int(guess[0]), int(guess[1]), int(guess[2])]


def give_hint(code, guess):

    for i in range(3):

        if guess[i] == code[i]:
            print(f"Digit {i + 1}: CORRECT ✓")

        elif guess[i] < code[i]:
            print(f"Digit {i + 1}: Too low ↑")

        else:
            print(f"Digit {i + 1}: Too high ↓")


def play_game():

    code = generate_code()
    attempts = 7

    print("""
=========================
       SECRET VAULT
=========================

A 3-digit code protects the vault.
You have 7 attempts to crack it.
""")

    while attempts > 0:

        print(f"\nAttempts remaining: {attempts}")

        guess = get_guess()

        if guess is None:
            continue

        if guess == code:
            print("\nACCESS GRANTED!")
            print("You cracked the vault.")
            return

        give_hint(code, guess)

        attempts -= 1

    print("\nACCESS DENIED!")
    print(f"The code was: {code[0]}{code[1]}{code[2]}")


play_game()