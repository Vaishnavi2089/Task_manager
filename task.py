class Task:
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.is_completed = False
    def __str__(self):
        status ="DONE" if self.is_completed else "PENDING"
        return f"[{self.id}] {self.title}: {status}"
