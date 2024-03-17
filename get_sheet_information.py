import requests
import json

def write_file(link):
    sheet_json = requests.get(link).json()
    print(sheet_json)
    with open("sheets.json", "w") as file:
        json.dump(sheet_json, file)

def read_file():
    with open("sheets.json", "r") as file:
        data = json.load(file)
    return data