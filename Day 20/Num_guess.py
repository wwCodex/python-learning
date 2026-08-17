import random 

def number_game():
    number = random.randint(1, 100)
    attempts = 0

    print(" Welcome to Target Number!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("\nYour guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")

        elif guess > number:
            print("Too high!")

        else:
            print(f"\nYou got it!")
            print(f"The number was {number}.")
            print(f"Attempts: {attempts}")
            break


number_game()