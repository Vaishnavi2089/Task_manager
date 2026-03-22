from task_manager import TaskManager

def main():
    manager = TaskManager()

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

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            manager.update_task(task_id)

        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            manager.delete_task(task_id)

        elif choice == "5":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()