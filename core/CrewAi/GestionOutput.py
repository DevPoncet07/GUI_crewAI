from PyQt6.QtCore import pyqtSignal, QObject
from pathlib import Path
from datetime import datetime
import os

class GestionOutput(QObject):
    text_log = pyqtSignal(str)
    status_agent=pyqtSignal(str,str)
    def __init__(self,boss):
        super().__init__()
        self.localPath = Path(__file__).parent.parent.parent
        self.boss=boss
        files=os.listdir(self.localPath/"save/logs")
        self.today = datetime.today().strftime('%Y-%m-%d')
        if not files:
            self.today+="_001.txt"
        else:
            file_id=0
            for index,f in enumerate(files):
                if file_id<=int(f[-7:-4]):
                    file_id=int(f[-7:-4])+1
            file_id=str("0"*(3-len(str(file_id)))+str(file_id))
            self.today+="_"+str(file_id)+".txt"
        self.file_name=self.localPath/"save/logs"/self.today
        file =open(self.file_name,"w").close()

    def write(self,text):
        self.text_log.emit(text)
        file =open(self.file_name,"a")
        file.write(text)
        file.close()


    def flush(self):
        pass

    def isatty(self):
        return False