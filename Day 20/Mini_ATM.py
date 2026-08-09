balance = 5000


def show_balance():
    print(f"\nYour balance: ₹{balance}")


def deposit():
    amount = int(input("\nEnter amount to deposit: ₹"))

    if amount <= 0:
        print("Invalid amount.")
        return

    global balance
    balance += amount
    print(f"₹{amount} deposited successfully.")


def withdraw():
    amount = int(input("\nEnter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        global balance
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")


def atm():
    print("=====================")
    print("      MINI ATM")
    print("=====================")

    while True:

        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank you for using Mini ATM!")
            break

        else:
            print("\nInvalid option.")


atm()