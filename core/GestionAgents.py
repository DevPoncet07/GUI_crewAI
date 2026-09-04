from pathlib import Path
import json

class GestionAgents:
    def __init__(self,boss):
        self.boss=boss
        self.path= Path(__file__).parent.parent

    def read_saved_data(self):
        with open(self.path/"save/data.json",'r') as f:
            data=json.load(f)
        return data

    def dump_saved_data(self,data):
        with open(self.path/"save/data.json",'w') as f:
            json.dump(data,f,indent=4)