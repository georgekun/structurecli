import os
from manager.BaseStructure import Base

from .spider_text import class_text as txt

class SpiderStructure(Base):
    
    def create_structure(self):
        os.mkdir("modules")
        os.chdir("modules")
        self._create_file("selenium_spider.py",txt)
        os.chdir("..")

    