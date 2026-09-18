from PyQt6.QtCore import QThread
from crewai import Agent, Task, Crew, Process, LLM
import contextlib

from core.ToolsList import ToolsList


class Runner(QThread):
    def __init__(self,boss,project,output,gestion_output):
        super().__init__()
        self.boss=boss
        self.output=output
        self.gestion_output=gestion_output
        self.project=project
        self.tools=ToolsList(project.path)


    def run(self):
        agents={}
        for agent in self.project.agents:
            llm=LLM(model=agent.model,base_url="http://localhost:11434")
            tools=[]
            for tool in self.tools.tools:
                tools.append(self.tools.tools[tool])
            agents[agent.role]=(Agent(role=agent.role,goal=agent.goal,backstory=agent.backstory,llm=llm,verbose=agent.verbose,tools=tools))
        tasks=[]
        for task in self.project.tasks:
            context=[]
            for e in task.context:
                context.append(tasks[e-1])
            tasks.append(Task(description=task.description,expected_output=task.expected_output,agent=agents[task.agent],context=context))
        list_agent=list(agents.values())

        with contextlib.redirect_stdout(self.gestion_output), contextlib.redirect_stderr(self.gestion_output):
            crew = Crew(agents=list_agent, tasks=tasks, process=Process.sequential, verbose=False)
            result = crew.kickoff(inputs={
                "demande": "Créer petit script en javascript dans un fichier math.js a la racine du projet, ce script doit contenir plusieurs fonctione mathematique de base, exportable  "})