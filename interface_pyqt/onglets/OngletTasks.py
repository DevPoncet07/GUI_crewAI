from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout,
)

from interface_pyqt.onglets.tasks.LayoutOneTask import LayoutOneTask

class OngletTasks(QWidget):
    def __init__(self,boss,project_focus):
        super().__init__()
        self.boss=boss
        self.projectFocus=project_focus
        self.layout = QVBoxLayout()

        self.container_tasks=QWidget()
        self.container_tasks.setProperty("class","OngletTasks--container_tasks")
        self.layout_tasks=QVBoxLayout()

        container_head_tasks=QWidget()
        container_head_tasks.setProperty("class","OngletTasks--container_head_tasks")
        layout_head_tasks=QHBoxLayout()

        label_order=QLabel("Ordre")
        layout_head_tasks.addWidget(label_order)
        label_order.setProperty("class","OngletTasks--label")
        label_order.setFixedWidth(100)

        label_description=QLabel("Description")
        layout_head_tasks.addWidget(label_description)
        label_description.setProperty("class","OngletTasks--label")
        label_description.setFixedWidth(500)

        label_agent=QLabel("Agent")
        layout_head_tasks.addWidget(label_agent)
        label_agent.setProperty("class","OngletTasks--label")
        label_agent.setFixedWidth(200)

        label_status=QLabel("Status")
        layout_head_tasks.addWidget(label_status)
        label_status.setProperty("class","OngletTasks--label")
        label_status.setFixedWidth(100)

        container_head_tasks.setLayout(layout_head_tasks)
        self.layout_tasks.addWidget(container_head_tasks)




        self.container_tasks.setLayout(self.layout_tasks)
        self.layout.addWidget(self.container_tasks)


        self.widgets_tasks=[]



        self.setLayout(self.layout)
        self.display_all_tasks()

    def display_all(self,project):
        self.projectFocus=project
        for widget in self.widgets_tasks:
            self.layout_tasks.removeWidget(widget)
            widget.deleteLater()
        self.widgets_tasks = []
        self.display_all_tasks()

    def display_all_tasks(self):
        for e in self.projectFocus.tasks:
            self.widgets_tasks.append(LayoutOneTask(e))
            self.layout_tasks.addWidget(self.widgets_tasks[-1])


