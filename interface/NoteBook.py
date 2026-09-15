from tkinter.ttk import Notebook

import customtkinter as ctk

from interface.FrameTache import FrameTache


class NoteBook(Notebook):
    def __init__(self,boss,run_task):
        self.boss=boss
        Notebook.__init__(self,master=boss)


        self.frame_tache=FrameTache(self,run_task)
        self.frame_execution = ctk.CTkFrame(self)
        self.frame_resulat = ctk.CTkFrame(self)

        self.add(self.frame_tache,text="Tâches")
        self.add(self.frame_execution, text="Exécutions")
        self.add(self.frame_resulat, text="Résultats")