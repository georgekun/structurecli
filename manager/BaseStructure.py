import os
import subprocess
import shutil 

from abc import ABC, abstractmethod

import manager.default_text as txt
from .default_decorator import time_dec
   
class Base(ABC):
    """Абстрактный класс для создания структуры"""
    name:str  # имя проекта

    def __init__(self, project_name):
        self.name = project_name

        print(f"CREATING PROJECT {self.name}...\n")
        os.mkdir(self.name)
        os.chdir(self.name)

        self.create_structure()
        self.__create_default_structure()

        os.chdir("..")
        print("\nDONE.")
        print("Проект создан с помощью StructureCli.")

   
    @abstractmethod
    def create_structure(self):
        pass

    def _create_file(self,file_name,default_text = "#this file was created using cli StructureCli"):
        with open(file_name, "w") as file:
            file.write(default_text)

    def __create_default_structure(self):
        self.__create_virtualenv()
        self.__create_decorator()
        self._create_file(".env","")
        self._create_file("main.py", txt.main_file)
        self._create_file(".gitignore",txt.gitignore)
        self._create_file("Dockerfile","FROM")
        self.__create_readme()
        self.__create_git()

   
    def __create_virtualenv(self):
        subprocess.run(["python3","-m", "venv", "venv"])

    def __create_git(self):
        subprocess.run(["git","init"])
        subprocess.run(["git", "add", "."])

    def __create_readme(self):
        self._create_file("README.md", f"{self.name} (version 0.1)")

    def __create_decorator(self):
        os.mkdir("utils")
        os.chdir("utils")
        self._create_file("decorators.py",time_dec)
        os.chdir("..")