from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit,
)

class OngletExecution(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.text_edit=QTextEdit()

        layout.addWidget(self.text_edit)

        self.setLayout(layout)

    def add_text(self,text):
        self.text_edit.append(text)