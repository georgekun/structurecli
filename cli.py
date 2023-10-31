import os
import argparse

from manager.spider.spider import SpiderStructure
from manager.telegram.telegram import TelegramBotStructure


def main():
    parser = argparse.ArgumentParser(description="CLI for project creation")
    parser.add_argument("path", help="Create a new project")
    parser.add_argument("create", help="Create a new project")
    parser.add_argument("name_structure", help="name project structue")
    parser.add_argument("name", help="Name of the project")

    args = parser.parse_args()
    
    path = args.path
    if not path:
        path = "/home/jordan/Desktop"
        
    os.chdir(path)
    if args.create == "create":
        if args.name_structure == "telegram":
           TelegramBotStructure(args.name)

        elif args.name_structure == "scrapy":
            SpiderStructure(args.name)
        else:
            print(f"Нет структуры {args.name_structure}")
    else:
        print(f"Неправильная команда {args.create}")


if __name__ == "__main__":
    main()