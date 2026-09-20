import os
from pathlib import Path
import json

from core.object.Project import Project
from core.object.Agent import Agent
from core.object.Task import Task


class GestionProjets:
    def __init__(self, boss):
        self.boss = boss
        self.path = Path(__file__).parent.parent

    def create_project(self, project):
        name_project = project['name'] + ".json"
        f = open(self.path / "save/projects" / name_project, "x")
        projet_json = '{\n    "name":"' + project['name'] + '",\n    "path": "' + project[
            "path"] + '",\n    "agents":[],\n    "tasks":[]\n}'
        f.write(projet_json)

    def get_all_project(self):
        files = os.listdir(self.path / "save/projects")
        projects=[]
        for file in files:
            projects.append(self.load_project(file[:-5]))
        return projects

    def load_project(self, name):
        name=name+".json"
        with open(self.path / "save/projects" / name, 'r') as f:
            data = json.load(f)
            agents = []
            for agent in data["agents"]:
                agents.append(Agent(agent))
            tasks = []
            for task in data["tasks"]:
                tasks.append(Task(task))
            project = Project(
                {"name": data["name"], "path": data['path'], "agents": agents, "tasks": tasks})
        return project

    def save_project(self, project):
        name_project = project.name + ".json"
        agents = []
        for agent in project.agents:
            agents.append({"role": agent.role, "goal": agent.goal, "backstory": agent.backstory, "model": agent.model,
                           "tools": agent.tools, "verbose": agent.verbose})
        tasks = []
        for task in project.tasks:
            tasks.append({"title": task.title, "order": task.order, "description": task.description,
                          "expected_output": task.expected_output, "context": task.context, "agent": task.agent})
        data = {"name": project.name, "path": project.path, "agents": agents, "tasks": tasks}
        with open(self.path / "save/projects" / name_project, 'w') as f:
            json.dump(data, f, indent=4)

    def delete_project(self, index):
        index += ".json"
        os.remove(self.path / "save/projects" / index)