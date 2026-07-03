import json
import os


os.makedirs("data", exist_ok=True)
#create karvands.json
path="data/karvands.json"
if not os.path.exists(path):
    data = {
        "bootcamp": {
            "title": "Karvand Python",
            "year": 2026
        },
        "karvands": []
    }

    with open(path,"w",encoding="utf-8") as file:
        json.dump(data,file,indent=2)
#create report.json
if not os.path.exists("data/report.json"):
    with open("data/report.json","w",encoding="utf-8") as file:
        json.dump([],file)


def Load_Data():
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        data = {
            "bootcamp": {
                "title": "Karvand Python",
                "year": 2026
            },
            "karvands": []
        }

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("JSON file was ReWrite.")

    return data

