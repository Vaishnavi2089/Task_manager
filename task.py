class Task:
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.is_done = False
    def __str__(self):
        status ="DONE" if self.is_done else "PENDING"
        return f"[{self.id}] {self.title}: {status}"
