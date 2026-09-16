# ui/dialogue_agent.py
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit,
    QTextEdit, QComboBox, QCheckBox, QDialogButtonBox
)


class DialogueNewAgent(QDialog):

    def __init__(self, parent=None, agent_existant: dict | None = None):
        super().__init__(parent)
        self.setWindowTitle("Modifier l'agent" if agent_existant else "Nouvel agent")
        self.setModal(True)  # bloque l'interaction avec la fenêtre parente tant qu'ouvert
        self.resize(420, 320)

        layout = QVBoxLayout(self)
        formulaire = QFormLayout()

        self.champ_role = QLineEdit()
        self.champ_goal = QTextEdit()
        self.champ_backstory = QTextEdit()
        self.champ_model = QComboBox()
        self.champ_model.addItems([
            "ollama/qwen2.5-coder:7b",
            "ollama/qwen2.5-coder:32b",
            "ollama/qwen3-coder:30b",
        ])
        self.champ_verbose = QCheckBox("Mode verbose")

        formulaire.addRow("Rôle :", self.champ_role)
        formulaire.addRow("Objectif :", self.champ_goal)
        formulaire.addRow("Backstory :", self.champ_backstory)
        formulaire.addRow("Modèle :", self.champ_model)
        formulaire.addRow("", self.champ_verbose)

        layout.addLayout(formulaire)

        # Pré-remplissage si on modifie un agent existant
        if agent_existant:
            self.champ_role.setText(agent_existant["role"])
            self.champ_goal.setPlainText(agent_existant["goal"])
            self.champ_backstory.setPlainText(agent_existant["backstory"])
            self.champ_model.setCurrentText(agent_existant["model"])
            self.champ_verbose.setChecked(agent_existant.get("verbose", True))

        # Boutons Annuler/Enregistrer standard
        boutons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        boutons.accepted.connect(self.accept)
        boutons.rejected.connect(self.reject)
        layout.addWidget(boutons)

    def donnees_agent(self) -> dict:
        """À appeler après un accept() pour récupérer les valeurs saisies."""
        return {
            "role": self.champ_role.text(),
            "goal": self.champ_goal.toPlainText(),
            "backstory": self.champ_backstory.toPlainText(),
            "model": self.champ_model.currentText(),
            "verbose": self.champ_verbose.isChecked(),
        }