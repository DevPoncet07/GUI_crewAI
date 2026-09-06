import customtkinter as ctk
from core.GestionProjet import GestionProjets
from core.GestionAgents import GestionAgents

from interface.MenuBar import MenuBar
from interface.ToplevelNewProject import TopLevelNewProject
from interface.TopLevelLoadProject import TopLevelLoadProject
from interface.TopLevelSaveAsProject import TopLevelSaveAsProject
from interface.TopLevelAi import TopLevelAi



class Root(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self.title("Mes agents")
        self.geometry("1000x1000")
        self.popup = None
        self.config(menu=MenuBar(self,self.open_toplevel_new_projet,self.save_project,self.open_toplevel_save_as_projets,self.open_toplevel_project,self.toplevel_ai,self.change_theme))

        self.gestionProjets=GestionProjets(self)
        self.projects=self.gestionProjets.read_saved_data()
        for project in self.projects:
            if project.focus:
                self.projectFocus=project
                self.title(self.projectFocus.name)
                break

        self.gestion_agents = GestionAgents(self)

    def open_toplevel_new_projet(self):
        self.popup = TopLevelNewProject(self, self.toplevel_new_project_create, self.toplevel_cancel)

    def toplevel_new_project_create(self,name,path):
        self.projectFocus=self.gestionProjets.create_project(name,path)
        self.projects = self.gestionProjets.read_saved_data()
        self.title(self.projectFocus.name)
        self.toplevel_cancel()

    def save_project(self):
        self.gestionProjets.dump_saved_data(self.projectFocus)

    def open_toplevel_save_as_projets(self):
        self.popup=TopLevelSaveAsProject(self,self.toplevel_save_as_project,self.toplevel_cancel)

    def toplevel_save_as_project(self,name):
        self.projectFocus.name=name
        self.gestionProjets.dump_saved_data(self.projectFocus)
        self.toplevel_cancel()

    def open_toplevel_project(self):
        self.popup = TopLevelLoadProject(self, self.projects, self.toplevel_projects_load, self.toplevel_cancel, self.toplevel_project_delete)

    def toplevel_projects_load(self,index):
        self.projectFocus=self.projects[index]
        self.title(self.projectFocus.name)
        self.gestionProjets.change_focus_project(self.projectFocus.name)
        self.popup.destroy()

    def toplevel_project_delete(self,index):
       self.gestionProjets.delete_project(self.projects[index].nampe)
       self.projects = self.gestionProjets.read_saved_data()
       self.projectFocus = {}
       for project in self.projects:
           if project.focus:
               self.projectFocus = project
               self.title(self.projectFocus.name)
               break


    def toplevel_ai(self):
        self.popup = TopLevelAi(self,self.toplevel_ai_save,self.toplevel_cancel,self.projectFocus.agents)

    def toplevel_ai_save(self,data):
        self.gestion_agents.dump_saved_data(data)
        self.popup.destroy()

    def toplevel_cancel(self):
        self.popup.destroy()

    def change_theme(self,theme):
        ctk.CTk._set_appearance_mode(self,mode_string=theme)

root=Root()
root.mainloop()

