from task_manager import TaskManager

def main():
    manager = TaskManager()
    manager.load_tasks()   # Load saved tasks at start

    while True:
        print("\n==== TASK MANAGER ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
            manager.save_tasks()

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID: "))
                manager.update_task(task_id)
                manager.save_tasks()
            except ValueError:
                print("❌ Please enter a valid number!")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID: "))
                manager.delete_task(task_id)
                manager.save_tasks()
            except ValueError:
                print("❌ Please enter a valid number!")

        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()