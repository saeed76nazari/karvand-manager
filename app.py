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


def Add_Karvand(id,name,email,city,degree,field,skill_name,skill_level,skill_score):
    data = Load_Data()
    new_karvand = {
        "id": id,
        "full_name": name,
        "email": email,
        "city": city,
        "education": {
            "degree": degree,
            "field_of_study": field
        },
        "skills": [
            {
                "name": skill_name,
                "level": skill_level,
                "score": skill_score
            }
        ]
    }
    data["karvands"].append(new_karvand)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def Show_All():
    data = Load_Data()

    if len(data["karvands"]) == 0:
        print("No karvand found.")
        return

    for karvand in data["karvands"]:
        print(f"ID: {karvand['id']}")
        print(f"Full Name: {karvand['full_name']}")
        print(f"Email: {karvand['email']}")
        print(f"City: {karvand['city']}")

        print("Education:")
        print(f"  Degree: {karvand['education']['degree']}")
        print(f"  field_of_study: {karvand['education']['field_of_study']}")

        print("Skills:")
        for skill in karvand["skills"]:
            print(f"  Name: {skill['name']}")
            print(f"  Level: {skill['level']}")
            print(f"  Score: {skill['score']}")

        print("=" * 30)
















data = Load_Data()
if data["karvands"]:
    id = data["karvands"][-1]["id"]
else:
    id = 0
####################################################################################
while True:
    
    msg="""
    1 ) Add
    2 ) All Show
    3 ) Search in id
    4 ) Search in skills *
    5 ) Edit
    6 ) Delete
    7 ) Report *
    8 ) Exit
    """
    msg_in=input(msg)
    if msg_in=="1":
        id+=1
        full_name=input("plase Enter is Full Name: ").strip()
        email=input("plase Enter is Email: ").strip()
        city=input("plase Enter is your city: ").strip()
        degree=input("plase Enter is your degree: ").strip()  #مدرک تحصیلی
        field_of_study=input("plase Enter is your field_of_study: ").strip() #رشته تحصیلی
        skill_name=input("plase Enter is skill_name: ").strip() #نام مهارت
        skill_level=input("plase Enter is skill_level: ").strip() #سطح مهارت 
#امتیاز مهارت
        while True:
            try:
                skill_score = int(input("Please Enter Skill Score (0-100): "))
                if 0 <= skill_score <= 100:
                    break
                else:
                    print("Error: Skill score in between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid number.")
        Add_Karvand(id,full_name,email,city,degree,field_of_study,skill_name,skill_level,skill_score)
    if msg_in=="2":
        Show_All()
    if msg_in=="3":
        pass
    if msg_in=="4":
        pass
    if msg_in=="5":
        pass
    if msg_in=="6":
        pass
    if msg_in=="7":
        pass
    if msg_in=="8":
        break