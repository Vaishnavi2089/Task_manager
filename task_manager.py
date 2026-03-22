from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    # Add Task
    def add_task(self, title):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        print("✅ Task added successfully!")

    # View Tasks
    def view_tasks(self):
        if not self.tasks:
            print("⚠️ No tasks available.")
            return

        print("\n📋 Your Tasks:")
        for task in self.tasks:
            print(task)
    # Update Task
    def update_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                print("1. Mark as Completed")
                print("2. Change Title")
                choice = input("Enter choice: ")

                if choice == "1":
                    task.is_completed = True
                    print("✅ Task marked as completed!")

                elif choice == "2":
                    new_title = input("Enter new title: ")
                    task.title = new_title
                    print("✏️ Task updated!")

                else:
                    print("❌ Invalid choice!")
                return

        print("⚠️ Task not found!")

    # Delete Task
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print("🗑️ Task deleted!")
                return

        print("⚠️ Task not found!")

    # Save tasks to file
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.id},{task.title},{task.is_completed}\n")

    # Load tasks from file
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task_id, title, is_completed = line.strip().split(",")

                    task = Task(int(task_id), title)
                    task.is_completed = is_completed == "True"

                    self.tasks.append(task)

                    # keep ID updated
                    if int(task_id) >= self.next_id:
                        self.next_id = int(task_id) + 1

        except FileNotFoundError:
            pass