import os 

from manager.BaseStructure import Base

class TelegramBotStructure(Base):

    def create_structure(self):
        os.mkdir("handlers")
        os.chdir("handlers")
        self._create_file("main_admin.py")
        self._create_file("main_client.py")
        os.chdir("..")

        os.mkdir("keyboards")
        os.chdir("keyboards")
        self._create_file("inline_keyboard.py")
        self._create_file("reply_keyboard.py")
        os.chdir("..")
