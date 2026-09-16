from PyQt6.QtWidgets import QHBoxLayout, QLabel


class LayoutOneTask(QHBoxLayout):
    def __init__(self,task):
        super().__init__()
        widget= QLabel(task.title)
        self.addWidget(widget)