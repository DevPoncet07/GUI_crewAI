import os
from pathlib import Path
import json

from core.Project import Project
from core.Agent import Agent
from core.Tasks import Tasks

class GestionProjets:
    def __init__(self,boss):
        self.boss=boss
        self.path= Path(__file__).parent.parent

    def create_project(self,name,path):
        self.change_focus_project()
        name_project=name+".json"
        f= open(self.path/"save/"/name_project,"x")
        projet_json='{\n    "name":"'+name+'",\n    "focus":true,\n    "path": "'+path+'",\n    "agents":[],\n  "taches":[]}'
        f.write(projet_json)
        project=Project({"name": name, "focus": True, "path": path, "agents": [],"taches":[]})
        return project

    def read_saved_data(self):
        files=os.listdir(str(self.path/"save"))
        projects=[]
        for file in files:
            with open(self.path/"save/"/file,'r') as f:
                data=json.load(f)
                focus=data["focus"]
                agents=[]
                for agent in data["agents"]:
                    agents.append(Agent(agent))
                tasks=[]
                for task in data["tasks"]:
                    tasks.append(Tasks(task))
                projects.append(Project({"name":data["name"],"focus":focus,"path":data['path'],"agents":agents,"tasks":tasks}))
        return projects

    def dump_saved_data(self,project):
        name_project=project.name+".json"
        agents=[]
        for agent in project.agents:
            agents.append({"role":agent.role,"goal":agent.goal,"backstory":agent.backstory,"model":agent.model,"tools":agent.tools,"verbose":agent.verbose})
        tasks=[]
        for task in project.tasks:
            tasks.append({"description":task.description})
        data={"name":project.name,"focus":project.focus,"path":project.path,"agents":agents,"tasks":tasks}
        with open(self.path/"save"/name_project,'w') as f:
            json.dump(data,f,indent=4)

    def delete_project(self,index):
        index+=".json"
        os.remove(self.path/"save/"/index)

    def change_focus_project(self,name=""):
        projects=self.read_saved_data()
        for project in projects:
            if project.name==name:
                project.focus=True
            else:
                project.focus=False
            self.dump_saved_data(project)




