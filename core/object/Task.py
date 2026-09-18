
class Task:
    def __init__(self,task):
        self.title=task["title"]
        self.description =task["description"]
        self.expected_output =task["expected_output"]
        self.agent =task["agent"]
        self.context=task["context"]
        self.order=task["order"]

    def __str__(self):
        return "Ordre : "+str(self.order)+"\n   title : "+self.title