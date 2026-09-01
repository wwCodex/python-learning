import json
import os

FILE = "data.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)

    return {
        "subjects": {},
        "attendance": {},
        "assignments": []
    }

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_subject(data):
    name = input("Subject name: ").title()

    if name in data["subjects"]:
        print("Subject already exists.\n")
        return

    marks = int(input("Marks: "))
    credits = int(input("Credits: "))

    data["subjects"][name] = {
        "marks": marks,
        "credits": credits
    }

    data["attendance"][name] = {
        "attended": 0,
        "total": 0
    }

    print("Subject added.\n")

def view_subjects(data):
    if not data["subjects"]:
        print("No subjects found.\n")
        return

    print("\n    SUBJECTS")

    for subject, info in data["subjects"].items():
        print(
            f"{subject:12} | Marks: {info['marks']} | Credits: {info['credits']}"
        )

    print()

def update_marks(data):
    subject = input("Subject: ").title()

    if subject not in data["subjects"]:
        print("Subject not found.\n")
        return

    marks = int(input("New marks: "))
    data["subjects"][subject]["marks"] = marks

    print("Marks updated.\n")

def grade_point(mark):
    if mark >= 90:
        return 10
    elif mark >= 80:
        return 9
    elif mark >= 70:
        return 8
    elif mark >= 60:
        return 7
    elif mark >= 50:
        return 6
    elif mark >= 40:
        return 5
    return 0

def calculate_gpa(data):
    if not data["subjects"]:
        print("No subjects.\n")
        return

    total_points = 0
    total_credits = 0

    for info in data["subjects"].values():
        gp = grade_point(info["marks"])
        total_points += gp * info["credits"]
        total_credits += info["credits"]

    gpa = total_points / total_credits

    print(f"\nYour GPA: {gpa:.2f}\n")

def record_attendance(data):
    subject = input("Subject: ").title()

    if subject not in data["attendance"]:
        print("Subject not found.\n")
        return

    attended = int(input("Classes attended: "))
    total = int(input("Total classes: "))

    data["attendance"][subject]["attended"] += attended
    data["attendance"][subject]["total"] += total

    print("Attendance updated.\n")

def view_attendance(data):
    print("\n    ATTENDANCE ")

    for subject, info in data["attendance"].items():
        total = info["total"]

        if total == 0:
            percent = 0
        else:
            percent = (info["attended"] / total) * 100

        warning = " ⚠" if percent < 75 else ""

        print(f"{subject:12} : {percent:.1f}%{warning}")

    print()

def add_assignment(data):
    title = input("Assignment title: ")
    due = input("Due date (YYYY-MM-DD): ")

    data["assignments"].append({
        "title": title,
        "due": due,
        "done": False
    })

    print("Assignment added.\n")

def view_assignments(data):
    if not data["assignments"]:
        print("No assignments.\n")
        return

    print("\n ASSIGNMENTS ")
    for i, task in enumerate(data["assignments"], start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']} ({task['due']})")

    print()

def complete_assignment(data):
    view_assignments(data)

    if not data["assignments"]:
        return

    num = int(input("Complete which number? "))

    if 1 <= num <= len(data["assignments"]):
        data["assignments"][num - 1]["done"] = True
        print("Completed.\n")
    else:
        print("Invalid number.\n")

def menu():
    print("""
 STUDENT DASHBOARD

1. Add Subject
2. View Subjects
3. Update Marks
4. Record Attendance
5. View Attendance
6. Add Assignment
7. View Assignments
8. Complete Assignment
9. Calculate GPA
0. Save & Exit

""")
def main():
    data = load_data()

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            add_subject(data)

        elif choice == "2":
            view_subjects(data)

        elif choice == "3":
            update_marks(data)

        elif choice == "4":
            record_attendance(data)

        elif choice == "5":
            view_attendance(data)

        elif choice == "6":
            add_assignment(data)

        elif choice == "7":
            view_assignments(data)

        elif choice == "8":
            complete_assignment(data)

        elif choice == "9":
            calculate_gpa(data)

        elif choice == "0":
            save_data(data)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid option.\n")

main()