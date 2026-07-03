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


def Search_Id(search_id):
    data = Load_Data()

    for karvand in data["karvands"]:
        if karvand["id"] == search_id:
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

            return

    print("No karvand found with the shenaseh.")



def Search_Skill(skill_name):
    data = Load_Data()
    found = False

    for karvand in data["karvands"]:
        for skill in karvand["skills"]:
            if skill["name"].lower() == skill_name.lower():
                found = True

                print(f"ID: {karvand['id']}")
                print(f"Full Name: {karvand['full_name']}")
                print(f"Email: {karvand['email']}")
                print(f"City: {karvand['city']}")
                print('-'*30)

    if not found:
        print("No karvand found with this skill.")



def Edit_Karvand(search_id):
    data = Load_Data()
    for karvand in data["karvands"]:
        if karvand["id"] == search_id:

            msg="""
                        1) Email
                        2) City
                        3) Degree
                        4) field_of_study
                """
            edit = input(f"this is select in {msg}: ")

            if edit == "1":
                karvand["email"] = input("New Email: ")
            elif edit == "2":
                karvand["city"] = input("New City: ")
            elif edit == "3":
                karvand["education"]["degree"] = input("New Degree: ")
            elif edit == "4":
                karvand["education"]["field_of_study"] = input("New field_of_study: ")

            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            print("information this edit  OK.")
            return
    print("No karvand found with the shenaseh.")


def Delete_Karvand(search_id):
    data = Load_Data()

    for karvand in data["karvands"]:
        if karvand["id"] == search_id:
            data["karvands"].remove(karvand)

            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            print("Karvand deleted  this  OK.")
            return

    print("No karvand found with the shenaseh.")


def Report():
    data = Load_Data()
    total_karvands = len(data["karvands"]) #تعداد کل کاروندها

    total_skills = 0 #تعداد کل مهار تهای ثب تشده
    total_score = 0 #میانگین امتیاز مهار تها
    cities = [] #فهرست شهرهای ثب تشده
    unique_skills = [] #فهرست مهارتهای غیرتکراری

    for karvand in data["karvands"]:

        # شهرها
        if karvand["city"] not in cities:
            cities.append(karvand["city"])

        # مهارت‌ها
        for skill in karvand["skills"]:
            total_skills += 1
            total_score += skill["score"]

            if skill["name"] not in unique_skills:
                unique_skills.append(skill["name"])

    if total_skills > 0:
        average_skill_score = total_score / total_skills
    else:
        average_skill_score = 0

    report = {
        "total_karvands": total_karvands,
        "total_skills": total_skills,
        "average_skill_score": average_skill_score,
        "cities": cities,
        "unique_skills": unique_skills
    }

    print(report)

    with open("data/report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)














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
        while True:
            try:
                search_id = int(input("Please Enter Search ID: "))
                break
            except ValueError:
                print("Please enter a of number.")
        Search_Id(search_id)
    if msg_in=="4":
        Search_Skill(input("Please Enter Search in Skill: "))
     if msg_in=="5":
        while True:
            try:
                search_id_edit = int(input("Plase Enter is id with the Edit:  "))
                break
            except ValueError:
                print("Please enter a of number.")
        Edit_Karvand(search_id_edit)
    if msg_in=="6":
        while True:
            try:
                search_id_del = int(input("Please Enter id this is karvand to delete : "))
                break
            except ValueError:
                print("Please enter a of number.")
        Delete_Karvand(search_id_del)
    if msg_in=="7":
        Report()
    if msg_in=="8":
        break