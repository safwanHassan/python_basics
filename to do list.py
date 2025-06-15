tasks = []

def show_menu():
    print("\n--- To-Do List ---\n1. View tasks\n2. Add task\n3. Delete task\n4. Exit")

def show_tasks():
    print("📭 No tasks." if not tasks else '\n'.join(f"{i+1}. {t}" for i, t in enumerate(tasks)))
    print()

def add_task():
    tasks.append(input("Enter task: "))
    print("✅ Task added!")

def delete_task():
    if not tasks:
        print("📭 No tasks to delete.")
        return
    show_tasks()
    try:
        i = int(input("Task number to delete: ")) - 1
        print(f"🗑 Deleted: {tasks.pop(i)}" if 0 <= i < len(tasks) else "❌ Invalid number.")
    except ValueError:
        print("❌ Enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1': show_tasks()
    elif choice == '2': add_task()
    elif choice == '3': delete_task()
    elif choice == '4':
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice.")