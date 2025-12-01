class SessionMemory:
    def __init__(self):
        self.memory = []

    def store(self, data):
        self.memory.append(data)

    def retrieve_all(self):
        return self.memory
