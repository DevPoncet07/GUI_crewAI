import customtkinter as ctk

class TopLevelValidation(ctk.CTkToplevel):
    def __init__(self,boss,title,validation,cancel):
        self.boss=boss
        ctk.CTkToplevel.__init__(self, master=self.boss)
        self.title(title)

        self.buttonValide=ctk.CTkButton(self,text="Validez",command=validation)
        self.buttonValide.pack(side="left",padx=20,pady=20)

        self.buttonCancel=ctk.CTkButton(self,text="Cancel",command=cancel)
        self.buttonCancel.pack(side="right",padx=20,pady=20)