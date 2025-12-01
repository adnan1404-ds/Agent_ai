class A2AProtocol:
    def send(self, sender, receiver, task):
        return {"from": sender, "to": receiver, "task": task}
