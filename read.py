from C import employee_dict
from prettytable import PrettyTable


""" This function is to view all the employees """
def view():
    if len(employee_dict) == 0:
        print(" NO DATA HAS BEEN SAVED")
    else:
        table = PrettyTable(["ID","Name","Age","Department","Salary","Skills","Email"])

        for k,v in employee_dict.items():
            table.add_row([k,v["name"],v["age"],v["department"],v["salary"],v["skill"],v["email"]])
        print(table)
    

""" This function is to search in data """

def search():
    print("""
              Search By

            1. Employee ID
            2. Name
            3. Department
    """)
    try:
        search_by = int(input("Search by : "))
        if search_by == 1:
            id = input("enter the employee ID : ").strip()

            if id in employee_dict:
                print(f"""
                Employee Found

                ID           :{id}
                Name         :{employee_dict[id]["name"]}
                Age          :{employee_dict[id]["age"]}
                Department   :{employee_dict[id]["department"]}
                Salary       :{employee_dict[id]["salary"]}
                Email        :{employee_dict[id]["email"]}
                    """)
            else:
                print("Employee not Found")


        elif search_by == 2:
            name = input("enter the name :").split().lower()
            flag =  0
            for k,v in employee_dict.items():
                if name == v["name"]:
                    print(f"""
                Employee Found

                ID           :{k}
                Name         :{employee_dict[k]["name"]}
                Age          :{employee_dict[k]["age"]}
                Department   :{employee_dict[k]["department"]}
                Salary       :{employee_dict[k]["salary"]}
                Email        :{employee_dict[k]["email"]}
                    """)
                    flag = 1
            if flag != 1:
                print("Employee not Found")

                
        
        elif search_by == 3:
            flag = 0
            depart = input("Enter the Department").strip().lower()
            table = PrettyTable(["ID","Name","Age","Department","Salary","Skills","Email"])
            for k,v in employee_dict.items():
                if depart == v["department"]:
                    table.add_row([k,v["name"],v["age"],v["department"],v["salary"],v["skill"],v["email"]])
                    flag = 1
                
            if flag != 1:
                print("Employee not Found")
            else:
                print(table)
        else:
            print("please enter correct value")
    except ValueError:
        print("Enter numeric value ")
    except Exception:
        print("Try again..")




""" This function is to create salary report """

def salary_report():
    salary = []
    for v in employee_dict.values():
        salary.append(v["salary"])
    print(salary)

    print(f"""
    
    ==========================  Salary Report ======================
    
    Highest Salary : {max(salary)}
    Lowest  Salary : {min(salary)}
    Average Salary : {sum(salary)//len(salary)}
    Total   Salary : {sum(salary)}
    Total Employee : {len(salary)}
    """)


""" This function is to get skill report """

def skill_report():
    skill ,skills = [],[]
    empl_python = []
    empl_django = []
    d = {}
    for v in employee_dict.values():
        skill += v["skill"].split(",")
        for i in skill:
            if i == "python":
                empl_python.append(v["name"])
            if i == "django":
                empl_django.append(v["name"])          
    for i in skill:
        if i not in skills:
            skills.append(i)
    for i in skills:
        d[i] = skill.count(i)
    result = sorted(d.items(),key = lambda x: x[1])
    print(f"""
    ================== Skill Report ==============================
    Total Unique Skills    : {len(skills)}
    Most Common Skills     : {result[-1][0]}""")
    print("    Employee having Python :")
    for i in empl_python:
        print(f"{i:^65}")
    print("    Employee having django : ")
    for i in empl_django:
        print(f"{i:^65}")


""" This function is to show department report """

def depart_report():
    all_depart,total_depart = [],[]
    for v in employee_dict.values():
        all_depart.append(v["department"])
        if v["department"] not in total_depart:
            total_depart.append(v["department"])
    print(f"""
    
    ==========================  Department Report ======================
    """)
    for i in total_depart:
        count = all_depart.count(i)
        print(f"{i:^25}: {count} employee ") if count <2 else print(f"{i:^25}: {count} employees ")
    


