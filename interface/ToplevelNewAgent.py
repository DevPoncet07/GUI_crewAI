from tkinter import StringVar

import customtkinter as ctk

class TopLevelNewAgent(ctk.CTkToplevel):
    def __init__(self,boss,save,cancel):
        self.boss=boss
        ctk.CTkToplevel.__init__(self,master=self.boss)
        self.title("Nouveau projet")

        self.file_path=""
        ctk.CTkLabel(self,text="Nom de l'agent").grid(row=0,column=0,padx=10,pady=10)
        self.varTextName=StringVar()
        self.entryName=ctk.CTkEntry(self,textvariable=self.varTextName)
        self.entryName.grid(row=0,column=1,padx=10,pady=10)
        self.entryName.focus_set()

        self.frame_button=ctk.CTkFrame(self)
        self.frame_button.grid(row=10,column=0,columnspan=2,padx=10,pady=10)
        self.button_save=ctk.CTkButton(self.frame_button, text="Crée",command=lambda:save(self.varTextName.get(),self.file_path))
        self.button_save.grid(row=0,column=0)
        self.button_cancel=ctk.CTkButton(self.frame_button, text="Cancel",command=lambda:cancel())
        self.button_cancel.grid(row=0,column=1)

