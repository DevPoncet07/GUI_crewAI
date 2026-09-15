from tkinter import StringVar
import customtkinter as ctk

from interface.TopLevelTask import TopLevelTask


class FrameTache(ctk.CTkFrame):
    def __init__(self,boss,run_task):
        self.boss=boss
        self.popup=None
        ctk.CTkFrame.__init__(self,master=boss)

        self.frame_bottom=ctk.CTkFrame(self)

        self.frame_loadingbar=LoadingBar(self.frame_bottom)
        self.frame_loadingbar.grid(row=0,column=0)

        self.button_run=ctk.CTkButton(self.frame_bottom,text="Run",command=run_task)
        self.button_run.grid(row=0,column=1)
        self.frame_bottom.grid(row=1,column=0,padx=10,pady=10)

        self.frame_top=ctk.CTkFrame(self)

        self.button_add_task=ctk.CTkButton(self.frame_top,text="Add Task",command=self.open_toplevel_task)
        self.button_add_task.grid(row=0,column=0,padx=10,pady=10)

        self.frame_tache_agent=FrameTacheAgent(self.frame_top)
        self.frame_tache_agent.grid(row=1,column=0,padx=10,pady=10)
        self.frame_top.grid(row=0,column=0,padx=10,pady=10)

    def open_toplevel_task(self):
        self.popup=TopLevelTask(self,self.add_task,self.cancel_toplevel,None)

    def add_task(self,data):
        print(data)
        self.cancel_toplevel()

    def cancel_toplevel(self):
        self.popup.destroy()

class FrameTacheAgent(ctk.CTkFrame):
    def __init__(self,boss):
        self.boss=boss
        ctk.CTkFrame.__init__(self,master=boss,width=400,height=400)

class LoadingBar(ctk.CTkFrame):
    def __init__(self,boss):
        self.boss=boss
        ctk.CTkFrame.__init__(self,master=boss,width=500)

        self.canvas=ctk.CTkCanvas(self,width=300,height=5,bg="black")
        self.canvas.grid(row=0,column=0)
        self.var_text=StringVar()
        self.var_text.set("loading ...")
        self.text=ctk.CTkLabel(self,textvariable=self.var_text)
        self.text.grid(row=1,column=0,sticky="w")


