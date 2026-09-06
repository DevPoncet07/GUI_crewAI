from tkinter import *

class MenuBar(Menu):
    def __init__(self,boss,new_projet,save_project,save_as_project,command_projet,commande_ai,command_theme):
        Menu.__init__(self,master=boss)

        self.menuProjet=Menu(self,tearoff=False)
        self.menuProjet.add_command(label="Nouveau...",command=new_projet)
        self.menuProjet.add_command(label="Save", command=save_project)
        self.menuProjet.add_command(label="Save as...", command=save_as_project)
        self.menuProjet.add_command(label="Charger...", command=lambda:command_projet())
        self.add_cascade(label="Projet",menu=self.menuProjet)

        self.commandAi=commande_ai
        self.add_command(label="Ai...",command=self.commandAi)

        self.commandTheme=command_theme
        self.menuTheme=Menu(self,tearoff=False)
        self.menuTheme.add_command(label="System Theme", command=lambda :self.commandTheme("system"))
        self.menuTheme.add_command(label="Light Theme",command=lambda: self.commandTheme("light"))
        self.menuTheme.add_command(label="Dark Theme",command=lambda :self.commandTheme("dark"))
        self.add_cascade(label="Theme",menu=self.menuTheme)

