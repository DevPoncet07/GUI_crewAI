from PyQt6.QtWidgets import QWidget, QScrollArea, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QProgressBar
from PyQt6.QtCore import Qt
from interface_pyqt.onglets.tasks.WidgetOneTask import WidgetOneTask


class WidgetTasks(QWidget):
    def __init__(self,project):
        super().__init__()
        self.project=project
        self.setFixedWidth(1000)
        self.layout = QVBoxLayout()

        layout_top=QHBoxLayout()
        button_add_task = QPushButton("Add Task")

        button_up_task=QPushButton("Up")

        button_down_task=QPushButton("Down")

        layout_top.addWidget(button_add_task)
        layout_top.addWidget(button_up_task)
        layout_top.addWidget(button_down_task)
        self.layout.addLayout(layout_top)

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


        layout_bottom=QHBoxLayout()
        self.progress_bar=QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(len(self.project.tasks))
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("%v / %m tâches terminées")
        layout_bottom.addWidget(self.progress_bar)

        button_run=QPushButton("Run")
        layout_bottom.addWidget(button_run)

        self.layout.addLayout(layout_bottom)
        self.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.widgets_tasks = []
        self.task_fous = None

    def display_all(self, project):
        self.project=project
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