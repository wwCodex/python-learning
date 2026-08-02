import random


def roll_dice():
    return random.randint(1, 6)


def player_turn():
    print("\n1. Normal Roll")
    print("2. Risky Roll")

    choice = input("Choose: ")

    if choice == "1":
        roll = roll_dice()
        print(f"You rolled: {roll}")
        return roll

    elif choice == "2":
        roll1 = roll_dice()
        roll2 = roll_dice()

        print(f"You rolled: {roll1} and {roll2}")

        # Double numbers are a lucky bonus
        if roll1 == roll2:
            print("LUCKY DOUBLE!")
            return roll1 + roll2 + 3

        return roll1 + roll2

    else:
        print("Invalid choice. Normal roll selected.")
        return roll_dice()


def computer_turn():
    roll = roll_dice()
    print(f"Computer rolled: {roll}")
    return roll


def play_game():

    player_score = 0
    computer_score = 0

    print("======================")
    print("      DICE DUEL")
    print("======================")
    print("First to 3 points wins!")

    while player_score < 3 and computer_score < 3:

        input("\nPress Enter to roll...")

        player_roll = player_turn()
        computer_roll = computer_turn()

        if player_roll > computer_roll:
            print("You win this round!")
            player_score += 1

        elif computer_roll > player_roll:
            print("Computer wins this round!")
            computer_score += 1

        else:
            print("DRAW!")

        print(f"\nYou: {player_score} | Computer: {computer_score}")

    if player_score == 3:
        print("\n YOU WON THE DICE DUEL!")
    else:
        print("\n COMPUTER WON!")

play_game()