import os
from pathlib import Path
import json

from core.GestionProjet import GestionProjets


class Core:
    def __init__(self):
        self.localPath=Path(__file__).parent
        with open(self.localPath/"config.json", 'r') as f:
            self.config = json.load(f)

        self.gestionProjet=GestionProjets(self)

        self.projectFocus=self.gestionProjet.load_project(self.config["project_focus"])
        print(self.projectFocus)

    def create_project(self,project):
        self.gestionProjet.create_project(project)
        self.projectFocus=self.gestionProjet.load_project(project['name']+".json")

    def load_project(self,name):
        self.projectFocus=self.gestionProjet.load_project(name)

    def get_all_projects(self):
        projects=self.gestionProjet.get_all_project()
        return projects

    def save_project(self):
        self.gestionProjet.save_project(self.projectFocus)
