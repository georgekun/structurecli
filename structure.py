import os
import argparse

from manager.spider.spider import SpiderStructure
from manager.telegram.telegram import TelegramBotStructure



if __name__ == "__main__":

    structure_list = ['telegram','scrapy']

    while True: 
        path = input("Input destination path: ")
        try: 
             os.chdir(path)
             break
        except:
             print("Path error.")
    
    while True:
        name = input("Input name project: ")
        if name:
            break
        else:
            print("Error. No name project. ")
        
    while True:
        print(f"All structures: {structure_list}")
        structure = input("Input type(structure) project: ")
        if structure in structure_list:
            break

    
    if  structure == "telegram":
        TelegramBotStructure(name)

    elif structure == "scrapy":
        SpiderStructure(name)

   