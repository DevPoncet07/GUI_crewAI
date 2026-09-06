from tkinter import StringVar

import customtkinter as ctk
from CTkListbox import *


class TopLevelAi(ctk.CTkToplevel):
    def __init__(self,boss,save,cancel,mes_agents):
        self.boss=boss
        self.mes_agents=mes_agents
        self.index=0
        ctk.CTkToplevel.__init__(self,master=self.boss)
        self.title("Mes agents")
        self.geometry("1000x1000")

        self.frame_list_agent=ctk.CTkFrame(self)
        self.frame_list_agent.grid(row=0,column=0,padx=10,pady=10)

        self.listbox_agent=CTkListbox(self.frame_list_agent,height=300,width=200)
        self.listbox_agent.grid(row=0,column=0,padx=10,pady=10)
        self.listbox_agent.bind("<ButtonRelease-1>",self.output_listbox_agents)

        self.frame_agent=ctk.CTkFrame(self)
        self.frame_agent.grid(row=0,column=1,padx=10,pady=10,ipadx=10,ipady=10)

        ctk.CTkLabel(self.frame_agent,text="Role").grid(row=0,column=0,padx=10,pady=10)
        self.varTextRole=StringVar()
        self.entry_role=ctk.CTkEntry(self.frame_agent,textvariable=self.varTextRole,width=300)
        self.entry_role.grid(row=0,column=1,padx=10,pady=10)

        self.button_save_agent=ctk.CTkButton(self.frame_agent, text="Save",command=self.save_agent)
        self.button_save_agent.grid(row=10,column=0)



        self.frame_button=ctk.CTkFrame(self)
        self.frame_button.grid(row=10,column=0,columnspan=2)
        self.button_save=ctk.CTkButton(self.frame_button, text="Valide",command=lambda:save(self.mes_agents))
        self.button_save.grid(row=0,column=0)
        self.button_cancel=ctk.CTkButton(self.frame_button, text="Cancel",command=lambda:cancel())
        self.button_cancel.grid(row=0,column=1)

        self.fill_listbox_agents()

    def fill_listbox_agents(self):
        self.listbox_agent.delete(0,'end')
        for e in self.mes_agents:
            print(e)
            self.listbox_agent.insert("END",e.role)

    def output_listbox_agents(self,_):
        self.index=self.listbox_agent.curselection()
        self.varTextRole.set(self.mes_agents[self.index].role)

    def save_agent(self):
        self.mes_agents[self.index].role=self.varTextRole.get()
        self.fill_listbox_agents()