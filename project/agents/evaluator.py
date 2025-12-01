class Evaluator:
    def evaluate(self, result):
        if result:
            return {"valid": True, "response": result}
        return {"valid": False, "response": "Invalid result"}
