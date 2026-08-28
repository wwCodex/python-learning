tasks = []

def add_task():
    title = input("\nTask: ").strip()
    priority = input("Priority (High/Medium/Low): ").title()
    task = {
        "title": title,
        "priority": priority,
        "done": False
    }
    tasks.append(task)
    print("Task added.")

def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks yet.")
        return
    print("\n========== TASKS ==========")

    for i in range(len(tasks)):
        status = "Done" if tasks[i]["done"] else "•"
        print(f"{i+1}. [{status}] {tasks[i]['title']} ({tasks[i]['priority']})")

def complete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    choice = int(input("\nComplete task number: ")) - 1
    if 0 <= choice < len(tasks):
        tasks[choice]["done"] = True
        print("Task completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    choice = int(input("\nDelete task number: ")) - 1
    if 0 <= choice < len(tasks):
        removed = tasks.pop(choice)
        print(f"Removed: {removed['title']}")
    else:
        print("Invalid task number.")

def search_task():
    keyword = input("\nSearch: ").lower()
    found = False
    for task in tasks:
        if keyword in task["title"].lower():
            status = "Done" if task["done"] else "Pending"
            print(f"\n{task['title']}")
            print(f"Priority : {task['priority']}")
            print(f"Status   : {status}")
            found = True
    if not found:
        print("No matching task found.")

def statistics():
    total = len(tasks)
    completed = 0
    for task in tasks:
        if task["done"]:
            completed += 1
    pending = total - completed
    print("\n========== STATS ==========")
    print(f"Total Tasks : {total}")
    print(f"Completed   : {completed}")
    print(f"Pending     : {pending}")
    if total != 0:
        percent = (completed / total) * 100
        print(f"Completion  : {percent:.1f}%")

def menu():
    while True:
        print("""
==============================
        TASKFLOW
==============================

1. Add Task
2. View Tasks
3. Complete Task
4. Search Task
5. Delete Task
6. Statistics
7. Exit
""")
        
        choice = input("Choose: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            search_task()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            statistics()

        elif choice == "7":
            print("\nSee you later.")
            break

        else:
            print("Invalid option.")

menu()