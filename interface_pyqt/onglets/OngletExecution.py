from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel,
)

class OngletExecution(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Suivi en temps réel"))

        self.setLayout(layout)