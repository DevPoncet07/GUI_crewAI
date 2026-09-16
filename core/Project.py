from core.Task import Task

class Project:
    def __init__(self,project):
        self.name=project["name"]
        self.path=project["path"]
        self.agents=project["agents"]
        self.tasks=project["tasks"]

    def add_task(self,task):
        task["order"]=len(self.tasks)
        self.tasks.append(Task(task))



    def update_task(self,task):
        print(task)



    def __str__(self):
        agents=""
        for agent in self.agents:
            agents+="   "+agent.__str__()+" \n"
        tasks=""
        for task in self.tasks:
            tasks+="   "+task.__str__()+" \n"
        return ("name : "+self.name +"\npath : "+self.path
                +"\nagents : \n"+str(agents[:-2])
                +"\ntasks : \n"+str(tasks[:-2]))
