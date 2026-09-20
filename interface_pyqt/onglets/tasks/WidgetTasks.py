from PyQt6.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from interface_pyqt.onglets.tasks.WidgetOneTask import WidgetOneTask


class WidgetTasks(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(1000)
        self.layout = QHBoxLayout()
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setProperty('class', 'WidgetTasks--scroll')
        self.scroll.viewport().setProperty( 'class', 'WidgetTasks--viewport')
        container = QWidget()
        container.setProperty('class', 'WidgetTasks--container_tasks')
        self.layout_tasks = QVBoxLayout()
        self.layout_tasks.setAlignment(Qt.AlignmentFlag.AlignTop)

        container_head_tasks = QWidget()
        container_head_tasks.setProperty("class", "WidgetTasks--container_head_tasks")
        container_head_tasks.setFixedHeight(35)
        layout_head_tasks = QHBoxLayout()

        label_order = QLabel("Ordre")
        layout_head_tasks.addWidget(label_order)
        label_order.setProperty("class", "OngletTasks--label")
        label_order.setFixedWidth(100)

        label_description = QLabel("Description")
        layout_head_tasks.addWidget(label_description)
        label_description.setProperty("class", "OngletTasks--label")
        label_description.setFixedWidth(500)

        label_agent = QLabel("Agent")
        layout_head_tasks.addWidget(label_agent)
        label_agent.setProperty("class", "OngletTasks--label")
        label_agent.setFixedWidth(200)

        label_status = QLabel("Status")
        layout_head_tasks.addWidget(label_status)
        label_status.setProperty("class", "OngletTasks--label")
        label_status.setFixedWidth(100)

        container_head_tasks.setLayout(layout_head_tasks)
        self.layout_tasks.addWidget(container_head_tasks)

        container.setLayout(self.layout_tasks)
        self.scroll.setWidget(container)
        self.layout.addWidget(self.scroll)
        self.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.widgets_tasks = []
        self.task_fous = None

    def display_all(self, project):
        for widget in self.widgets_tasks:
            self.layout_tasks.removeWidget(widget)
            widget.deleteLater()
        self.widgets_tasks = []
        for task in project.tasks:
            self.widgets_tasks.append(WidgetOneTask(task,self))
            self.layout_tasks.addWidget(self.widgets_tasks[-1])

    def change_task_focus(self, task):
        self.task_fous=task
        for widget in self.widgets_tasks:
            widget.setProperty("class","")
            if widget.task.order == task.order:
                widget.setProperty("class", "WidgetOneTasks--selected")
            widget.style().unpolish(widget)
            widget.style().polish(widget)