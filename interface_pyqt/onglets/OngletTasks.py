from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
)

from interface_pyqt.onglets.tasks.LayoutOneTask import LayoutOneTask

class OngletTasks(QWidget):
    def __init__(self,boss,project_focus):
        super().__init__()
        self.boss=boss
        self.projectFocus=project_focus
        self.layout = QVBoxLayout()

        self.widgets_tasks=[]



        self.setLayout(self.layout)
        self.display_all_tasks()

    def display_all(self,project):
        self.projectFocus=project
        for widget in self.widgets_tasks:
            self.boss.delete_children_layout(widget)
            self.layout.removeItem(widget)
        self.widgets_tasks.clear()
        self.display_all_tasks()

    def display_all_tasks(self):
        for e in self.projectFocus.tasks:
            self.widgets_tasks.append(LayoutOneTask(e))
            self.layout.addLayout(self.widgets_tasks[-1])


