class Worker:
    def __init__(self, tools):
        self.tools = tools

    def execute(self, task):
        task_type = task.get("task_type")
        content = task.get("content")
        if task_type == "classification":
            return self.tools.classify(content)
        elif task_type == "summarization":
            return self.tools.summarize(content)
        elif task_type == "action_extraction":
            return self.tools.extract_actions(content)
        return "Unknown task"
