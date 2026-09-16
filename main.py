import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget,QDialog,
)

from core.Core import Core
from interface_pyqt.dialogues.DialogueLoadProject import DialogueLoadProject
from interface_pyqt.dialogues.DialogueNewProject import DialogueNewProject
from interface_pyqt.MenuBar import MenuBar

from interface_pyqt.onglets.OngletExecution import OngletExecution
from interface_pyqt.onglets.OngletTasks import OngletTasks


class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()

        self.core=Core()
        self.setWindowTitle("CrewIa - "+str(self.core.projectFocus.name))


        self.menu = MenuBar(self)
        self.setMenuBar(self.menu)


        self.onglets = QTabWidget()

        self.onglet_task = OngletTasks(self,self.core.projectFocus)
        self.onglet_execution=OngletExecution()

        self.onglets.addTab(self.onglet_task, "Tâches")
        self.onglets.addTab(self.onglet_execution, "Execution")

        self.setCentralWidget(self.onglets)

    def create_new_project(self):
        dialogue = DialogueNewProject(self)
        result= dialogue.exec()
        if result == QDialog.DialogCode.Accepted:
            new_project= dialogue.donnees_project()
            self.core.create_project(new_project)
            self.setWindowTitle("CrewIa - " + str(self.core.projectFocus.name))

    def load_project(self):
        projects=self.core.get_all_projects()
        dialogue = DialogueLoadProject(self,projects)
        result = dialogue.exec()
        if result == QDialog.DialogCode.Accepted:
            project = dialogue.donnees_project()
            self.core.load_project(project.name)
            self.setWindowTitle("CrewIa - " + str(self.core.projectFocus.name))
            self.onglet_task.display_all(self.core.projectFocus)

    def save_project(self):
        self.core.save_project()

    def delete_children_layout(self,layout):
        while layout.count():
            item=layout.takeAt(0)
            print(item)
            widget=item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                sous_layout=item.layout()
                if sous_layout is not None:
                    self.delete_children_layout(sous_layout)
if __name__ == "__main__":

    app = QApplication(sys.argv)

    with open("interface_pyqt/style.qss", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = FenetrePrincipale()

    screen = app.screens()[0]
    geometry_ecran = screen.availableGeometry()
    x= geometry_ecran.x() + int((geometry_ecran.width() - window.width()) / 2)
    y = geometry_ecran.y() + int((geometry_ecran.height() - window.height()) / 2)

    # Move window to calculated coordinates
    window.move(x, y)
    window.show()
    sys.exit(app.exec())
