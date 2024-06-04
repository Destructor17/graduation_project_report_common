import json
import os


def check_config():
    if not os.path.exists("config.json"):
        print("Необходимо создать файл config.json")
        exit(1)
    with open("config.json") as file:
        try:
            config = json.load(file)
        except json.JSONDecodeError:
            print("Ошибка при загрузке config.json")
            exit(1)


def prerun_checks():
    check_config()
