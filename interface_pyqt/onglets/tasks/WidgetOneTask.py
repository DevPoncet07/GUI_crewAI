from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QWidget


class WidgetOneTask(QWidget):
    def __init__(self,task,boss):
        super().__init__()
        self.boss=boss
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.layout=QHBoxLayout()
        self.task=task

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

    def mousePressEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:
            self.boss.change_task_focus(self.task)

    def mouseDoubleClickEvent(self, event):
        print("ok")