from tkinter import StringVar

import customtkinter as ctk
from CTkListbox import *

from interface.ToplevelValidation import TopLevelValidation


class TopLevelLoadProject(ctk.CTkToplevel):
    def __init__(self,boss,projects,load,cancel,delete):
        self.boss=boss
        self.index=0
        self.projects=projects
        self.delete=delete
        self.popup=None
        ctk.CTkToplevel.__init__(self,master=self.boss)
        self.title("Mes projets")

        self.frameListboxProjet=ctk.CTkFrame(self)
        self.listboxProject=CTkListbox(self.frameListboxProjet,height=300,width=200)
        self.listboxProject.grid(row=0,column=0)
        self.listboxProject.bind("<<ListboxSelect>>",self.output_listbox_projects)
        self.frameListboxProjet.grid(row=0,column=0,padx=10,pady=10)

        self.frameProject=ctk.CTkFrame(self)
        self.frameProject.grid(row=0,column=1,padx=10,pady=10)

        self.varTextName=StringVar()
        ctk.CTkLabel(self.frameProject,text="Nom du projet").grid(row=0,column=0)
        self.entryName=ctk.CTkEntry(self.frameProject,textvariable=self.varTextName,state='disabled')
        self.entryName.grid(row=0,column=1)

        ctk.CTkLabel(self.frameProject,text="Agents du projet").grid(row=1,column=0,columnspan=2)
        self.frameAgent=ctk.CTkFrame(self.frameProject,width=250,height=250)
        self.frameAgent.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
        self.frameAgent.grid_propagate(False)
        self.frameAgent.columnconfigure(0,weight=1)

        self.buttonDelete=ctk.CTkButton(self.frameProject,text="Supprimer le projet",command=self.open_toplevel_validation)
        self.buttonDelete.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

        self.frame_button=ctk.CTkFrame(self)
        self.frame_button.grid(row=10,column=0,columnspan=2,padx=10,pady=10)
        self.button_save=ctk.CTkButton(self.frame_button, text="Charger",command=lambda:load(self.index))
        self.button_save.grid(row=0,column=0)
        self.button_cancel=ctk.CTkButton(self.frame_button, text="Cancel",command=lambda:cancel())
        self.button_cancel.grid(row=0,column=1)

        self.fill_listbox_project()

    def fill_listbox_project(self):
        self.listboxProject.delete(0,'end')
        for e in self.projects:
            self.listboxProject.insert("END",e.name)

    def output_listbox_projects(self,_):
        self.index=self.listboxProject.curselection()
        self.varTextName.set(self.projects[self.index].name)
        self.display_agents(self.projects[self.index].agents)

    def display_agents(self,agents):
        index=1
        for child in self.frameAgent.winfo_children():
            child.destroy()
        for agent in agents:
            ctk.CTkLabel(self.frameAgent,text=agent.role).grid(row=index,column=0)
            index+=1

    def open_toplevel_validation(self):
        self.popup=TopLevelValidation(self.boss,"Supprimer le projet",self.validation,self.cancel)

    def validation(self):
        self.delete(self.index)
        self.projects=self.boss.projects
        self.fill_listbox_project()
        self.varTextName.set(self.projects[0].name)
        self.display_agents(self.projects[0].agents)
        self.popup.destroy()

    def cancel(self):
        self.popup.destroy()

