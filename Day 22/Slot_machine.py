import random 


def spin():
    symbols = ["1", "2", "3", "4", "5", "6"]

    result = []

    for i in range(3):
        result.append(random.choice(symbols))

    return result


def check_result(result):

    if result[0] == result[1] == result[2]:
        if result[0] == "6":
            print("JACKPOT! ")
            return 100

        print("THREE OF A KIND!")
        return 50

    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        print("Two matching symbols!")
        return 20

    else:
        print("Nothing this time.")
        return 0


def play():

    balance = 100

    print("======================")
    print("    SLOT MACHINE")
    print("======================")
    print("Starting balance: $100")

    while balance > 0:

        print(f"\nBalance: ${balance}")

        choice = input("Spin for $10? (y/n): ").lower()

        if choice != "y":
            break

        balance -= 10

        result = spin()

        print("\n | ".join(result))

        winnings = check_result(result)

        balance += winnings

    print(f"\nFinal balance: ${balance}")

    if balance == 0:
        print("You went broke!")

    else:
        print("Thanks for playing!")


play()