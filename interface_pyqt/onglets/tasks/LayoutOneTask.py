from PyQt6.QtWidgets import QHBoxLayout, QLabel, QWidget


class LayoutOneTask(QWidget):
    def __init__(self,task):
        super().__init__()

        self.layout=QHBoxLayout()

        label_order = QLabel(str(task.order))
        self.layout.addWidget(label_order)
        label_order.setProperty("class", "OngletTasks--label")
        label_order.setFixedWidth(100)

        label_description = QLabel(task.description)
        self.layout.addWidget(label_description)
        label_description.setProperty("class", "OngletTasks--label")
        label_description.setFixedWidth(500)

        label_agent = QLabel(task.agent)
        self.layout.addWidget(label_agent)
        label_agent.setProperty("class", "OngletTasks--label")
        label_agent.setFixedWidth(200)

        label_status = QLabel("None")
        self.layout.addWidget(label_status)
        label_status.setProperty("class", "OngletTasks--label")
        label_status.setFixedWidth(100)

        self.setLayout(self.layout)