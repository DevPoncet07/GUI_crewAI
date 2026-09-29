import os
from pathlib import Path
from crewai.tools import tool

class ToolsList:
    def __init__(self,path):
        self.path=path
        self.tools={"list_dir":self.create_listdir_folder_tool(),
                    "read_file":self.create_read_file_tool(),
                    "create_file":self.create_create_file_tool(),
                    "write_file":self.create_write_file_tool(),
                    "edit_file":self.create_edit_file_tool()}



    def create_listdir_folder_tool(self):
        base_path = self.path

        @tool("Lister les fichiers et dossiers du projet")
        def listdir_folder_tool(path):
            """
                Liste les fichiers et dossiers présents dans un dossier du projet.

                Utilise cet outil lorsque tu dois explorer la structure du projet,
                savoir quels fichiers existent ou vérifier le contenu d'un dossier.

                Le chemin fourni doit être relatif à la racine du projet.
                Utilise "." pour lister le contenu de la racine du projet.

                N'utilise pas cet outil pour lire le contenu d'un fichier.
                Pour lire un fichier, utilise l'outil read_file.

                Args:
                    path (str) : Chemin du dossier relatif à la racine du projet.
            """
            folder_path=base_path+"/"+path
            print("Path of folder : "+folder_path)
            is_dir=os.listdir(folder_path)
            if not is_dir:
                return base_path+ " n'est pas un dossier"
            files=[]
            for file in os.listdir(folder_path):
                if file.startswith(".") or file.startswith("__"):
                    pass
                else:
                    files.append(file)
            return files
        return listdir_folder_tool


    def create_read_file_tool(self):
        base_path = self.path

        @tool("Lire le contenu d'un fichier du projet")
        def read_file_tool(path):
            """
                Lit et retourne le contenu complet d'un fichier du projet.

                Utilise cet outil avant de modifier un fichier existant afin de
                connaître son contenu actuel.

                Utilise également cet outil après une modification pour vérifier
                que la modification a bien été effectuée.

                Le chemin fourni doit être relatif à la racine du projet.

                N'utilise pas cet outil pour lister les fichiers d'un dossier.
                Pour cela, utilise l'outil list_dir.

                Args:
                    path (str) : Chemin du fichier relatif à la racine du projet.
            """
            print("Path of folder : " + base_path+path)
            with open(base_path+"/"+path) as f:
                content=f.read()
            return content
        return read_file_tool


    def create_create_file_tool(self):
        base_path = self.path

        @tool("Créer un nouveau fichier dans le projet")
        def create_file_tool(path,content):
            """
                Crée réellement un nouveau fichier dans le projet avec le contenu fourni.

                Utilise cet outil lorsqu'une tâche demande de créer un fichier qui
                n'existe pas encore.

                Le fichier est immédiatement écrit sur le disque.
                Ne te contente pas de retourner le contenu du fichier dans ta réponse :
                utilise cet outil pour créer réellement le fichier.

                Le chemin doit être relatif à la racine du projet.

                Args:
                    path (str) : Chemin du fichier relatif à la racine du projet.
                    content (str) : Contenu complet du nouveau fichier.
            """
            print("Path of folder : " + base_path+path)
            with open(base_path+"/"+path, "w", encoding="utf-8") as f:
                f.write(content)
            return path+" à bien été crée"
        return create_file_tool


    def create_write_file_tool(self):
        base_path = self.path
        @tool("Écrire ou remplacer complètement le contenu d'un fichier")
        def write_file_tool(path,content):
            """
                Remplace entièrement le contenu d'un fichier existant.

                Utilise cet outil lorsque tu dois réécrire complètement un fichier.

                Attention : le contenu actuel du fichier sera entièrement remplacé.
                Si tu dois seulement modifier une partie du fichier, utilise plutôt
                l'outil edit_file.

                Le chemin doit être relatif à la racine du projet.

                Args:
                    path (str) : Chemin du fichier relatif à la racine du projet.
                    content (str) : Nouveau contenu complet du fichier.
            """
            print("Path of folder : " + base_path+path)
            with open(base_path+"/"+path, "w", encoding="utf-8") as f:
                f.write(content)
            return "le texte a bien été écris"
        return write_file_tool

    def create_edit_file_tool(self):
        base_path = self.path

        @tool("Modifier une partie précise d'un fichier")
        def edit_file_tool(path, old_content, new_content):
            """
                Modifie une partie précise d'un fichier existant.

                Utilise cet outil lorsqu'une tâche demande de modifier, ajouter ou
                remplacer une partie du code d'un fichier existant.

                Le texte fourni dans old_content doit correspondre exactement à une
                partie existante du fichier.

                Seule la première occurrence de old_content sera remplacée.

                Utilise read_file avant cet outil pour connaître le contenu actuel
                du fichier et identifier précisément la partie à modifier.

                Après la modification, utilise read_file pour vérifier que la
                modification a bien été effectuée.

                Le chemin doit être relatif à la racine du projet.

                Args:
                    path (str) : Chemin du fichier relatif à la racine du projet.
                    old_content (str) : Contenu exact actuellement présent dans le fichier.
                    new_content (str) : Nouveau contenu qui doit remplacer old_content.
            """
            file_path = os.path.join(base_path, path)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            if old_content not in content:
                return "ERREUR : le contenu à remplacer n'existe pas dans le fichier."

            content = content.replace(old_content, new_content, 1)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            return f"{path} a été modifié avec succès."
        return edit_file_tool