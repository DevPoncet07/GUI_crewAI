
class Tasks:
    def __init__(self,tache):
        self.description =tache["description"]
        self.expected_output =tache["expected_output"]
        self.agent =tache["agent"]
        self.context=tache["context"]