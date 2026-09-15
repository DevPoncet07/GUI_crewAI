import os
from pathlib import Path

class ToolsList:
    def __init__(self):
        self.tools=[
            Tool(name="listdir",function=listdir_folder_tool),
        Tool(name="create_file",function=create_file_tool),]


class Tool:
    def __init__(self,name,function):
        self.name=name
        self.function=function



def listdir_folder_tool(path):
    folder_path=Path(path)
    is_dir=os.path.isdir(folder_path)
    if not is_dir:
        return path+ "n'est pas un dossier"
    files=[]
    for file in os.listdir(folder_path):
        files.append(file)
    return files



def create_file_tool(path,name,content):
    pathname=path+name
    os.makedirs(os.path.dirname(pathname), exist_ok=True)
    with open(pathname, "w", encoding="utf-8") as f:
        f.write(content)