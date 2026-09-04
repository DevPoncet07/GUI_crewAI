import customtkinter as ctk
from CTkListbox import *

class TopLevelAi(ctk.CTkToplevel):
    def __init__(self,boss,save,cancel,mes_agents):
        self.boss=boss
        self.mes_agents=mes_agents
        print(self.mes_agents)
        ctk.CTkToplevel.__init__(self,master=self.boss)
        self.title("Mes agents")
        self.geometry("300x300")

        self.frame_list_agent=ctk.CTkFrame(self)
        self.frame_list_agent.grid(row=0,column=0,padx=10,pady=10)

        self.listbox_agent=CTkListbox(self.frame_list_agent)
        self.listbox_agent.grid(row=0,column=0,padx=10,pady=10)





        self.frame_button=ctk.CTkFrame(self)
        self.frame_button.grid(row=10,column=0,columnspan=2)
        self.button_save=ctk.CTkButton(self.frame_button, text="Valide",command=lambda:save(self.mes_agents))
        self.button_save.grid(row=0,column=0)
        self.button_cancel=ctk.CTkButton(self.frame_button, text="Cancel",command=lambda:cancel())
        self.button_cancel.grid(row=0,column=1)

        self.fill_listbox_agents()

    def fill_listbox_agents(self):
        for e in self.mes_agents:
            print(e)
            self.listbox_agent.insert("END",e['title'])