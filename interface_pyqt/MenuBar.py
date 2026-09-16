from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtCore import pyqtSignal


class MenuBar(QMenuBar):
    def __init__(self,boss):
        self.boss=boss
        super().__init__(boss)

        menu = self.addMenu("Projet")
        menu.addAction("Nouveau").triggered.connect(self.boss.create_new_project)
        menu.addAction("Sauvegarder").triggered.connect(self.boss.save_project)
        menu.addAction("Charger...").triggered.connect(self.boss.load_project)
