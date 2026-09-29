from PyQt6.QtCore import QThread
from crewai import Agent, Task, Crew, Process, LLM
import contextlib


from core.CrewAi.Listener import listener
from core.ToolsList import ToolsList



class Runner(QThread):
    def __init__(self, boss, project, gestion_output):
        super().__init__()
        self.boss = boss
        self.gestion_output = gestion_output
        self.project = project
        self.tools = ToolsList(project.path)

    def make_agents(self):
        agents = {}
        for agent in self.project.agents:
            llm = LLM(model=agent.model, base_url="http://localhost:11434")
            tools = []
            for tool in agent.tools:
                print(tool)
                tools.append(self.tools.tools[tool])
            agents[agent.role] = (
                Agent(role=agent.role, goal=agent.goal, backstory=agent.backstory, llm=llm, verbose=agent.verbose,
                      tools=tools))
        return agents

    def exec_task(self, agent, description, expected_output):
        task = Task(description=description, expected_output=expected_output, agent=agent)
        crew = Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=False)
        resultat = crew.kickoff()
        return str(resultat)

    def exact_task(self, texte_plan: str) -> list[str]:
        return [
            ligne.replace("SOUS_TACHE:", "", 1).strip()
            for ligne in texte_plan.splitlines()
            if ligne.strip().startswith("SOUS_TACHE:")
        ]

    def run(self):
        listener.worker_actif = self.gestion_output
        agents = self.make_agents()
        try:
            with contextlib.redirect_stdout(self.gestion_output), contextlib.redirect_stderr(self.gestion_output):
                chef_project = agents['Chef de project']
                plan_brut = self.exec_task(
                    chef_project,
                    description=(
                        "Découpe cette demande en sous-tâches de CODE uniquement pour qu'un agent de développement puisse effectuer la tache — chaque sous-tâche doit "
                        "résulter en un fichier créé ou modifié. N'inclus PAS de sous-tâches d'analyse "
                        "('identifier', 'vérifier', 'analyser', 'déterminer') — fais cette analyse toi-même "
                        "avant d'écrire le plan, en utilisant tes outils correctement (utilise list-dir pour chercher les dossiers et fichiers) de lecture, puis ne liste que "
                        "les actions de code concrètes qui en résultent.\n\n"
                        f"Demande :"
                        
                        "\n\nFORMAT OBLIGATOIRE : pas de markdown, juste du text, une sous-tâche par ligne, commençant par 'SOUS_TACHE: '. "
                        "Chaque ligne doit décrire une action de code précise : quel fichier créer ou "
                        "modifier, et quoi y ajouter exactement."
                    ),
                    expected_output="Une liste de lignes commençant par 'SOUS_TACHE: '",
                )
                sous_taches = self.exact_task(plan_brut)
                self.gestion_output.write(f"\n{len(sous_taches)} sous-tâches identifiées\n")
                resultats = []
                for i, sous_tache in enumerate(sous_taches, start=1):
                    self.gestion_output.write(f"\n--- Sous-tâche {i}/{len(sous_taches)} ---\n")
                    """agent_focus=None
                    for a in self.project.agents:
                        if a.role=="Développeur":
                            agent_focus=a
                    llm = LLM(model=agent_focus.model, base_url="http://localhost:11434")
                    tools =[]
                    for tool in  agent_focus.tools:
                        tools.append(self.tools.tools[tool])
                    agent=Agent(
                        role=agent_focus.role, goal=agent_focus.goal, backstory=agent_focus.backstory,
                        llm=llm, verbose=agent_focus.verbose, tools=tools,
                    )"""

                    resultat = self.exec_task(
                        agents["Développeur"],
                        description=f"Implémente dan le code EXACTEMENT cette sous-tâche, et rien d'autre, utilise les outils mis a disposition.\n\n"
                                    f"sous-tâche : {sous_tache}\n\n",
                        expected_output="Confirmation précise du fichier modifié ou créé et de ce qui a été fait",
                    )
                    resultats.append(resultat)


        except Exception as exc:
            self.gestion_output.write(f"\nErreur fatale : {exc}\n")
        finally:
            listener.worker_actif = None
