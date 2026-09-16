
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