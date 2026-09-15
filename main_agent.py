from crewai import Agent, Task, Crew, Process, LLM

# Un LLM par rôle, pointant sur ton Ollama local
llm_pm      = LLM(model="ollama/qwen2.5-coder:7b",  base_url="http://localhost:11434")
llm_coder   = LLM(model="ollama/qwen3-coder:30b",   base_url="http://localhost:11434")
llm_tester  = LLM(model="ollama/qwen2.5-coder:7b",  base_url="http://localhost:11434")
llm_review  = LLM(model="ollama/qwen2.5-coder:32b", base_url="http://localhost:11434")

chef_projet = Agent(
    role="Chef de projet technique",
    goal="Découper une demande fonctionnelle en tâches de dev claires et ordonnées",
    backstory="Tu es un lead technique qui découpe les specs en tickets précis, sans ambiguïté.",
    llm=llm_pm,
    verbose=True,
)

codeur = Agent(
    role="Développeur",
    goal="Écrire du code fonctionnel et propre qui répond au ticket fourni",
    backstory="Développeur web senior, tu écris du code testable et documenté.",
    llm=llm_coder,
    verbose=True,
)

testeur = Agent(
    role="Testeur QA",
    goal="Vérifier que le code fonctionne réellement et remonter les bugs précisément",
    backstory="Tu exécutes le code, tu ne devines jamais s'il marche.",
    llm=llm_tester,
    verbose=True,
)

reviewer = Agent(
    role="Reviewer senior",
    goal="Relire le code pour la qualité, la sécurité et les bonnes pratiques",
    backstory="Tu es exigeant sur la lisibilité, la sécurité et la maintenabilité.",
    llm=llm_review,
    verbose=True,
)

task_plan = Task(
    description="Découpe cette demande en tâches de dev : {demande}",
    expected_output="Une liste de tâches numérotées avec critères d'acceptation",
    agent=chef_projet,
)

task_code = Task(
    description="Implémente les tâches définies",
    expected_output="Le code source complet des fichiers concernés",
    agent=codeur,
    context=[task_plan],
)

task_test = Task(
    description="Exécute les tests sur le code produit et rapporte les échecs",
    expected_output="Rapport de test : succès/échec avec détails",
    agent=testeur,
    context=[task_code],
)

task_review = Task(
    description="Relis le code en tenant compte du rapport de test",
    expected_output="Liste de remarques de review, ou validation finale",
    agent=reviewer,
    context=[task_code, task_test],
)

crew = Crew(
    agents=[chef_projet, codeur, testeur, reviewer],
    tasks=[task_plan, task_code, task_test, task_review],
    process=Process.sequential,
    verbose=True,
)

result = crew.kickoff(inputs={"demande": "Créer petit script en javascript dans un fichier math.js dans le dossier Mes_ia, ce script doit contenir plusieurs fonctione mathematique de base, exportable  "})