from datetime import datetime


notes = []


def show_help():
    print("""
Available commands:

help      - Show available commands
time      - Show current time
about     - About this system
calc      - Simple calculator
notes     - View saved notes
addnote   - Add a note
clear     - Clear the screen
shutdown  - Shut down the system
""")


def show_time():
    current_time = datetime.now()
    print(f"\nCurrent time: {current_time.strftime('%H:%M:%S')}")


def about():
    print("""
OS v1.0

A small terminal environment
built entirely with Python.

System status: ONLINE
Developer: wwCodex
""")


def calculator():

    print("\nCALCULATOR")

    number1 = float(input("First number: "))
    operator = input("Operator (+, -, *, /): ")
    number2 = float(input("Second number: "))

    if operator == "+":
        result = number1 + number2

    elif operator == "-":
        result = number1 - number2

    elif operator == "*":
        result = number1 * number2

    elif operator == "/":

        if number2 == 0:
            print("Cannot divide by zero.")
            return

        result = number1 / number2

    else:
        print("Unknown operator.")
        return

    print(f"Result: {result}")


def show_notes():

    print("\nNOTES")

    if len(notes) == 0:
        print("No notes saved.")

    else:
        for note in notes:
            print("-", note)


def add_note():

    note = input("\nWrite your note: ")

    notes.append(note)

    print("Note saved.")


def clear_screen():

    print("\n" * 40)


def shutdown():

    print("""
       SYSTEM SHUTDOWN

Saving session...
Closing processes...
Goodbye.
""")

    return False


def start_system():

    print("""
================================
OS v1.0
================================

System boot complete.
Welcome.
Type 'help' for commands.
""")

    running = True

    while running:

        command = input("\nOS> ").lower()

        if command == "help":
            show_help()

        elif command == "time":
            show_time()

        elif command == "about":
            about()

        elif command == "calc":
            calculator()

        elif command == "notes":
            show_notes()

        elif command == "addnote":
            add_note()

        elif command == "clear":
            clear_screen()

        elif command == "shutdown":
            running = shutdown()

        elif command == "":
            continue

        else:
            print("Unknown command.")
            print("Type 'help' to see available commands.")


start_system()