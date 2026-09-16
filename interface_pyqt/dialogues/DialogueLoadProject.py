
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QDialogButtonBox, QListWidget)


class DialogueLoadProject(QDialog):

    def __init__(self,boss,projects):
        super().__init__(boss)
        self.setWindowTitle("Nouveau projet")
        self.setModal(True)
        self.projects=projects
        self.project=projects[0].name

        layout = QVBoxLayout(self)

        self.listbox_projects=QListWidget()
        for project in projects:
            self.listbox_projects.addItem(project.name)
        self.listbox_projects.currentItemChanged.connect(self.output_listbox_project)


        layout.addWidget(self.listbox_projects)

        boutons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        boutons.accepted.connect(self.accept)
        boutons.rejected.connect(self.reject)
        layout.addWidget(boutons)

    def output_listbox_project(self):
        self.project=self.projects[self.listbox_projects.currentRow()]
        print(self.project)


    def donnees_project(self):
        return self.project