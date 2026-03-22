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