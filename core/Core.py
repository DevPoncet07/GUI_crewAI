
from pathlib import Path
import json

from core.CrewAi.GestionOutput import GestionOutput
from core.GestionProjet import GestionProjets
from core.CrewAi.Runner import Runner


class Core:
    def __init__(self,boss):
        self.boss=boss
        self.localPath=Path(__file__).parent
        with open(self.localPath/"config.json", 'r') as f:
            self.config = json.load(f)
        self.gestionProjet=GestionProjets(self)
        self.projectFocus=self.gestionProjet.load_project(self.config["project_focus"])

    def create_project(self,project):
        self.gestionProjet.create_project(project)
        self.projectFocus=self.gestionProjet.load_project(project['name'])

    def load_project(self,name):
        self.projectFocus=self.gestionProjet.load_project(name)
        self.config["project_focus"]=name
        with open(self.localPath/"config.json", 'w') as f:
            json.dump(self.config,f,indent=4)
    def get_all_projects(self):
        projects=self.gestionProjet.get_all_project()
        return projects

    def save_project(self):
        self.gestionProjet.save_project(self.projectFocus)


    def change_order_task(self,task,direction):
        last_order=task.order
        if direction=="up":
            if last_order==1:
                pass
            else:
                del self.projectFocus.tasks[last_order-1]
                self.projectFocus.tasks.insert(last_order-2,task)

        if direction=="down":
            if last_order==len(self.projectFocus.tasks):
                pass
            else:
                del self.projectFocus.tasks[last_order-1]
                self.projectFocus.tasks.insert(last_order,task)
        index = 1
        for task in self.projectFocus.tasks:
            task.order=index
            index+=1
        self.save_project()


    def run_all(self):
        self.gestion_output = GestionOutput(self.boss)
        self.gestion_output.nouveau_texte.connect(self.boss.onglet_execution.ajouter_texte)
        self.runner = Runner(self,self.projectFocus,self.boss.onglet_execution.ajouter_texte,self.gestion_output)
        self.runner.start()

    def stop_all(self):
        self.runner.terminate()


