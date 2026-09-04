from tkinter import *

import customtkinter
import customtkinter as ctk

from interface.MenuBar import MenuBar
from interface.TopLevelAi import TopLevelAi

from core.GestionAgents import GestionAgents


class Root(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self.title("Mes agents")
        self.geometry("500x500")
        self.popup = None
        self.config(menu=MenuBar(self,self.toplevel_ai,self.change_theme))

        self.gestion_agents = GestionAgents(self)
        self.gestion_agents.read_saved_data()
        self.mes_agents=self.gestion_agents.read_saved_data()

    def change_theme(self,theme):
        ctk.CTk._set_appearance_mode(self,mode_string=theme)

    def toplevel_ai(self):
        self.popup = TopLevelAi(self,self.toplevel_ai_save,self.toplevel_ai_cancel,self.mes_agents)

    def toplevel_ai_save(self,data):
        self.gestion_agents.dump_saved_data(data)
        self.popup.destroy()

    def toplevel_ai_cancel(self):
        self.popup.destroy()

root=Root()
root.mainloop()

