from tkinter import *

class MenuBar(Menu):
    def __init__(self,boss,commande_ai,command_theme):
        Menu.__init__(self,master=boss)

        self.commandAi=commande_ai
        self.add_command(label="Ai",command=self.commandAi)

        self.commandTheme=command_theme
        self.menuTheme=Menu(self,tearoff=False)
        self.menuTheme.add_command(label="System Theme", command=lambda :self.commandTheme("system"))
        self.menuTheme.add_command(label="Light Theme",command=lambda: self.commandTheme("light"))
        self.menuTheme.add_command(label="Dark Theme",command=lambda :self.commandTheme("dark"))
        self.add_cascade(label="Theme",menu=self.menuTheme)

