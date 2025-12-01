class ContextEngineering:
    def compact(self, text):
        return text[:100] + "..." if len(text) > 100 else text
