class Tools:
    def classify(self, text):
        return "Action Required"

    def summarize(self, text):
        return text[:50] + "..." if len(text) > 50 else text

    def extract_actions(self, text):
        return ["Extract key tasks from email"]
