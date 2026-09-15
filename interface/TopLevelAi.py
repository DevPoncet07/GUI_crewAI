from tkinter import StringVar, END

import customtkinter as ctk
from CTkListbox import *

from interface.ToplevelNewAgent import TopLevelNewAgent
from interface.ToplevelValidation import TopLevelValidation
from core.Agent import Agent


class TopLevelAi(ctk.CTkToplevel):
    def __init__(self,boss,save,cancel,mes_agents,tools):
        self.boss=boss
        self.mes_agents=mes_agents
        self.tools=tools
        self.index=0
        ctk.CTkToplevel.__init__(self,master=self.boss)
        self.title("Mes agents")

        self.frame_list_agent=ctk.CTkFrame(self)
        self.frame_list_agent.grid(row=0,column=0,padx=10,pady=10)

        self.listbox_agent=CTkListbox(self.frame_list_agent,height=300,width=200)
        self.listbox_agent.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
        self.listbox_agent.bind("<ButtonRelease-1>",self.output_listbox_agents)

        self.button_add_agent=ctk.CTkButton(self.frame_list_agent,text="Ajouter",command=self.new_agent)
        self.button_add_agent.grid(row=1,column=0,padx=10,pady=10)

        self.button_delete_agent = ctk.CTkButton(self.frame_list_agent, text="Supprimer",command=self.delete_agent)
        self.button_delete_agent.grid(row=1, column=1, padx=10, pady=10)

        self.frame_agent=ctk.CTkFrame(self)
        self.frame_agent.grid(row=0,column=1,padx=10,pady=10,ipadx=10,ipady=10)

        ctk.CTkLabel(self.frame_agent,text="Role").grid(row=0,column=0,padx=10,pady=10)
        self.varTextRole=StringVar()
        self.entry_role=ctk.CTkEntry(self.frame_agent,textvariable=self.varTextRole,width=400)
        self.entry_role.grid(row=0,column=1,padx=10,pady=10)

        ctk.CTkLabel(self.frame_agent, text="Model").grid(row=1, column=0, padx=10, pady=10)
        self.varTextModel = StringVar()
        self.entry_model= ctk.CTkEntry(self.frame_agent, textvariable=self.varTextModel, width=400)
        self.entry_model.grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkLabel(self.frame_agent, text="Goal").grid(row=2, column=0, padx=10, pady=10)
        self.entry_goal = ctk.CTkTextbox(self.frame_agent, width=400)
        self.entry_goal.grid(row=2, column=1, padx=10, pady=10)

        ctk.CTkLabel(self.frame_agent, text="Backstory").grid(row=3, column=0, padx=10, pady=10)
        self.entry_backstory = ctk.CTkTextbox(self.frame_agent, width=400)
        self.entry_backstory.grid(row=3, column=1, padx=10, pady=10)

        self.frame_tool=ctk.CTkFrame(self.frame_agent)
        self.frame_tool.grid(row=4,column=0,columnspan=2,padx=10,pady=10)
        ctk.CTkLabel(self.frame_tool,text='Tools').grid(row=0,column=0,columnspan=3,padx=10,pady=10)

        self.frame_tool_left=ctk.CTkFrame(self.frame_tool)
        self.frame_tool_left.grid(row=1,column=0,padx=10,pady=10)
        ctk.CTkLabel(self.frame_tool_left,text='Actif').grid(row=0,column=0,padx=10,pady=10)
        self.listbox_agent_tool=CTkListbox(self.frame_tool_left,height=100,width=200)
        self.listbox_agent_tool.grid(row=1,column=0,padx=10,pady=10)

        self.frame_tool_center = ctk.CTkFrame(self.frame_tool)
        self.frame_tool_center.grid(row=1, column=1, padx=10, pady=10)
        self.button_add_tool=ctk.CTkButton(self.frame_tool_center,text="Ajouter")
        self.button_add_tool.grid(row=0,column=0,padx=5,pady=5)
        self.button_delete_tool = ctk.CTkButton(self.frame_tool_center, text="Supprimer")
        self.button_delete_tool.grid(row=1, column=0, padx=5, pady=5)

        self.frame_tool_right = ctk.CTkFrame(self.frame_tool)
        self.frame_tool_right.grid(row=1, column=2, padx=10, pady=10)
        ctk.CTkLabel(self.frame_tool_right, text='Disponible').grid(row=0, column=0, padx=10, pady=10)
        self.listbox_dispo_tool = CTkListbox(self.frame_tool_right, height=100, width=200)
        self.listbox_dispo_tool.grid(row=1, column=0, padx=10, pady=10)


        self.button_save_agent=ctk.CTkButton(self.frame_agent, text="Sauvegarder",command=self.save_agent)
        self.button_save_agent.grid(row=10,column=0,columnspan=2)

        self.frame_button=ctk.CTkFrame(self)
        self.frame_button.grid(row=10,column=0,columnspan=2,padx=10,pady=10)
        self.button_save=ctk.CTkButton(self.frame_button, text="Valide",command=lambda:save(self.mes_agents))
        self.button_save.grid(row=0,column=0,padx=5,pady=5)
        self.button_cancel=ctk.CTkButton(self.frame_button, text="Cancel",command=lambda:cancel())
        self.button_cancel.grid(row=0,column=1,padx=5,pady=5)

        self.fill_listbox_agents()
        self.fill_listbox_dispo_tool()

    def fill_listbox_agents(self):
        self.listbox_agent.delete(0,'end')
        for e in self.mes_agents:
            self.listbox_agent.insert('end',e.role)

    def output_listbox_agents(self,_):
        self.index=self.listbox_agent.curselection()
        self.varTextRole.set(self.mes_agents[self.index].role)
        self.varTextModel.set(self.mes_agents[self.index].model)
        self.entry_goal.delete(0.0, 'end')
        self.entry_goal.insert(END, self.mes_agents[self.index].goal)
        self.entry_backstory.delete(0.0, 'end')
        self.entry_backstory.insert(END, self.mes_agents[self.index].backstory)

    def fill_listbox_dispo_tool(self):
        print(self.tools)
        for tool in self.tools:
            self.listbox_dispo_tool.insert(END,tool.name)


    def save_agent(self):
        self.mes_agents[self.index].role=self.varTextRole.get()
        self.mes_agents[self.index].model=self.varTextModel.get()
        self.mes_agents[self.index].goal=self.entry_goal.get(0.0,END)
        self.mes_agents[self.index].backstory=self.entry_backstory.get(0.0,END)
        self.fill_listbox_agents()

    def new_agent(self):
        self.popup=TopLevelNewAgent(self,self.add_new_agent,self.cancel_toplevel)

    def cancel_toplevel(self):
        self.popup.destroy()

    def add_new_agent(self,name,model):
        self.mes_agents.append(Agent({"role":name,"model":model,"backstory":"","goal":"","tools":[],"verbose":True}))
        self.fill_listbox_agents()
        self.cancel_toplevel()

    def delete_agent(self):
        self.popup=TopLevelValidation(self,"supprimer l'agent "+self.mes_agents[self.index].role+"?",self.validation_delete_agent,self.cancel_toplevel)

    def validation_delete_agent(self):
        del self.mes_agents[self.index]
        self.fill_listbox_agents()
        self.cancel_toplevel()