
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLineEdit, QCheckBox, QDialogButtonBox, QFileDialog,
                             QPushButton)


class DialogueNewProject(QDialog):

    def __init__(self,boss):
        super().__init__(boss)
        self.setWindowTitle("Nouveau projet")
        self.setModal(True)
        self.dir_path=""

        layout = QVBoxLayout(self)
        formulaire = QFormLayout()

        self.champ_name = QLineEdit()
        self.champ_name.setObjectName("DialogueNewProject--entry-name")
        self.champ_path = QPushButton(text="Choisir")
        self.champ_path.clicked.connect(self.choice_path)

        self.champ_verbose = QCheckBox("Mode verbose")

        formulaire.addRow("Nom :", self.champ_name)
        formulaire.addRow("Chemin :", self.champ_path)


        layout.addLayout(formulaire)

        boutons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        boutons.accepted.connect(self.accept)
        boutons.rejected.connect(self.reject)
        layout.addWidget(boutons)

    def choice_path(self):
        self.dir_path = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Select directory",
            directory="/home/adrien",
            options=QFileDialog.Option.DontUseNativeDialog,
        )
        self.champ_path.setText(self.dir_path)

    def donnees_project(self) -> dict:
        """À appeler après un accept() pour récupérer les valeurs saisies."""
        return {
            "name": self.champ_name.text(),
            "path": self.dir_path,
        }