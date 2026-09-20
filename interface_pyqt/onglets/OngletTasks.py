from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout
)

from PyQt6.QtCore import Qt

from interface_pyqt.onglets.tasks.WidgetTasks import WidgetTasks

class OngletTasks(QWidget):
    def __init__(self,boss,project_focus):
        super().__init__()
        self.boss=boss
        self.projectFocus=project_focus
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.widget_tasks=WidgetTasks()
        self.layout.addWidget(self.widget_tasks)

        self.layout_tasks=QVBoxLayout()
        self.layout_tasks.setAlignment(Qt.AlignmentFlag.AlignCenter)


        container_bottom=QWidget()
        layout_bottom=QHBoxLayout()
        container_bottom.setLayout(layout_bottom)

        self.layout.addWidget(container_bottom)


        self.setLayout(self.layout)


        self.widget_tasks.display_all(project=self.projectFocus)



