
class Agent:
    def __init__(self,agent):
        self.role =agent["role"]
        self.goal = agent["goal"]
        self.backstory = agent["backstory"]
        self.model = agent["model"]
        self.tools = agent["tools"]
        self.verbose = agent["verbose"]

    def __str__(self):
        return "name : "+self.role

    def return_dict(self):
        return {
            "name":self.role,
            "goal":self.goal,
            "backstory":self.backstory,
            "llm":self.model,
            "verbose":self.verbose,
        }