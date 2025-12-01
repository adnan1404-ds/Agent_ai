class Planner:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_type, content):
        task = {"task_type": task_type, "content": content}
        self.tasks.append(task)
        return task

    def get_tasks(self):
        return self.tasks
