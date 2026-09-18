import os
from pathlib import Path
from crewai.tools import tool

class ToolsList:
    def __init__(self,path):
        self.path=path
        self.tools={"list_dir":self.create_listdir_folder_tool(),
                    "read_file":self.create_read_file_tool(),
                    "create_file":self.create_create_file_tool(),
                    "write_file":self.create_write_file_tool()}



    def create_listdir_folder_tool(self):
        base_path = self.path

        @tool("Lister les fichiers d'un dossier")
        def listdir_folder_tool(path):
            """Liste les fichiers présents dans un dossier.
            Args:
            path (str) : chemin du dossier depuis la racine du projet"""
            folder_path=base_path+"/"+path
            print("Path of folder : "+folder_path)
            is_dir=os.listdir(folder_path)
            if not is_dir:
                return base_path+ "n'est pas un dossier"
            files=[]
            for file in os.listdir(folder_path):
                files.append(file)
            return files
        return listdir_folder_tool


    def create_read_file_tool(self):
        base_path = self.path

        @tool("Lire le contenus d'un fichier")
        def read_file_tool(path):
            """Lit et retourne le contenu d'un fichier.
                    Args:
                    path (string) : chemin du dossier depuis la racine du projet. """
            print("Path of folder : " + base_path+path)
            with open(base_path+"/"+path) as f:
                content=f.read()
            return content
        return read_file_tool


    def create_create_file_tool(self,):
        base_path = self.path

        @tool("Crée un fichier")
        def create_file_tool(path,name,content):
            """Crée un fichier avec le contenu fourni.
                    Args:
                    path (string) : chemin du fichier depuis la racine du projet
                    name (string) : nom du fichier
                    content (string) : contenu du fichier
                    """
            print("Path of folder : " + base_path+path+name)
            with open(base_path+"/"+path+"/"+name, "w", encoding="utf-8") as f:
                f.write(content)
            return name+"à bien été crée"
        return create_file_tool


    def create_write_file_tool(self):
        base_path = self.path
        @tool("Ajouter du contenus a un fichier")
        def write_file_tool(path,name,content):
            """ajoute du contenu à un fichier fourni.
            Args:
            path (string) : chemin du fichier depuis la racine du projet
            name (string) : nom du fichier
            content (string) : contenu du fichier"""
            print("Path of folder : " + base_path+path)
            with open(base_path+"/"+path+"/"+name, "w", encoding="utf-8") as f:
                f.write(content)
            return "le text a bien été écris"
        return write_file_tool