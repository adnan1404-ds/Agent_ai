from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.tools.tools import Tools
from project.memory.session_memory import SessionMemory
from project.core.context_engineering import ContextEngineering
from project.core.observability import Observability
from project.core.a2a_protocol import A2AProtocol

class MainAgent:
    def __init__(self):
        self.tools = Tools()
        self.planner = Planner()
        self.worker = Worker(self.tools)
        self.evaluator = Evaluator()
        self.memory = SessionMemory()
        self.context = ContextEngineering()
        self.logger = Observability()
        self.protocol = A2AProtocol()

    def handle_message(self, message):
        self.logger.log(f"Received message: {message}")
        task = self.planner.create_task("summarization", message)
        sent_task = self.protocol.send("Planner", "Worker", task)
        result = self.worker.execute(sent_task["task"])
        eval_result = self.evaluator.evaluate(result)
        self.memory.store({"input": message, "output": eval_result})
        return {"response": eval_result["response"]}

def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result["response"]
