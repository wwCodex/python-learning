expenses = {}


def add_expense():
    name = input("What did you spend on? ").lower()
    amount = float(input("How much did it cost? ₹"))

    expenses[name] = amount
    print("Expense added!")


def show_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n----- EXPENSES -----")

    total = 0

    for item in expenses:
        print(f"{item.title()} : ₹{expenses[item]}")
        total += expenses[item]

    print("--------------------")
    print(f"Total spent: ₹{total}")


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")