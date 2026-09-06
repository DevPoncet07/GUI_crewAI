from tkinter import StringVar

import customtkinter as ctk



class TopLevelSaveAsProject(ctk.CTkToplevel):
    def __init__(self,boss,save,cancel):
        self.boss=boss
        self.index=0
        self.popup=None
        ctk.CTkToplevel.__init__(self,master=self.boss)
        self.title("Mes projets")

        self.varTextName=StringVar()
        ctk.CTkLabel(self,text="Name").grid(row=0,column=0,padx=10,pady=10)
        self.entryName=ctk.CTkEntry(self,textvariable=self.varTextName).grid(row=0,column=1,padx=10,pady=10)



        self.frame_button=ctk.CTkFrame(self)
        self.frame_button.grid(row=10,column=0,columnspan=2,padx=10,pady=10)
        self.button_save=ctk.CTkButton(self.frame_button, text="Sauvegarder",command=lambda:save(self.varTextName))
        self.button_save.grid(row=0,column=0)
        self.button_cancel=ctk.CTkButton(self.frame_button, text="Cancel",command=lambda:cancel())
        self.button_cancel.grid(row=0,column=1)



    def cancel(self):
        self.popup.destroy()

