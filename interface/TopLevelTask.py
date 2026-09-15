from tkinter import StringVar,END

import customtkinter as ctk

class TopLevelTask(ctk.CTkToplevel):
    def __init__(self,boss,save,cancel,task):
        self.boss=boss
        self.projects=task
        self.save=save
        ctk.CTkToplevel.__init__(self,master=self.boss)


        self.frame_description=ctk.CTkFrame(self)
        self.frame_description.grid(row=0,column=0)
        ctk.CTkLabel(self.frame_description,text="Description").grid(row=0,column=0)
        self.text_area_description=ctk.CTkTextbox(self.frame_description,width=300)
        self.text_area_description.grid(row=1,column=0)

        self.frame_resultat = ctk.CTkFrame(self)
        self.frame_resultat.grid(row=1, column=0)
        ctk.CTkLabel(self.frame_resultat, text="Résultat").grid(row=0, column=0)
        self.text_area_resultat= ctk.CTkTextbox(self.frame_resultat, width=300)
        self.text_area_resultat.grid(row=1, column=0)


        self.frame_agent = ctk.CTkFrame(self)
        self.frame_agent.grid(row=2, column=0)
        ctk.CTkLabel(self.frame_agent, text="Agent").grid(row=0, column=0)
        self.var_text_combobox=ctk.StringVar(value="1")
        self.select_box=ctk.CTkComboBox(self.frame_agent,width=200,values=["1","2"],variable=self.var_text_combobox)
        self.select_box.grid(row=1, column=0)

        self.frame_depend = ctk.CTkFrame(self)
        self.frame_depend.grid(row=3, column=0)
        ctk.CTkLabel(self.frame_depend, text="Context").grid(row=0, column=0)
        self.checkbox_1 = ctk.CTkCheckBox(self.frame_depend,text="1")
        self.checkbox_1.grid(row=1, column=0)

        self.frame_button = ctk.CTkFrame(self)
        self.frame_button.grid(row=4, column=0)

        self.button_add=ctk.CTkButton(self.frame_button,text="Add",command=self.add)
        self.button_add.grid(row=0, column=0)

        self.button_cancel=ctk.CTkButton(self.frame_button, text="Cancel",command=cancel)
        self.button_cancel.grid(row=0,column=1)
        self.title("Taches")

    def add(self):
        context=[]
        if self.checkbox_1.get():
            context.append("1")
        data={
            "description":self.text_area_description.get(0.0,END),
            "excepted_output":self.text_area_resultat.get(0.0,END),
            "agent":self.var_text_combobox.get(),
            "context":context}
        self.save(data)