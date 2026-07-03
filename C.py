

employee_dict = {}

""" This is the decorator for getting viewing employee data table before executing the function """

def View_detail(func):
    def add_feature():
        from read import view
        view()
        return func()
    return add_feature

""" This is used to check existing data stored in file"""

def data_check(d):
    try:
        d = {}
        data = []
        with open("Data.txt","r") as f:
            for i in f:
                data = i.split("     ")
                if data[0] not in employee_dict:
                    d[data[0]] = eval(data[1]) # I have used eval() to convert string of dict to dict     #### but i can also use ast.literal_eval()   
    except Exception:
        print(" error occur")
    return d



""" This function is to create add data """

def Add_employee():
    d = {}
    d = data_check(d)
    data_entering = True
    while data_entering:
        employee_id = input("Enter Employee ID :").strip().lower()
        if employee_id in employee_dict or employee_id in d:
            print("Entered id already exist")
            continue
        if employee_id == "":
            print("please enter employee id")
            continue
        data_entering = False
    

    data_entering = True
    while data_entering:
        name = input("Enter Name :").strip().lower()
        if name == "":
            print("Name should not be empty")
            continue
        data_entering = False
    
    data_entering = True
    while data_entering:
        try :
            age = int(input("Enter Age :"))
        except Exception:
            print("please enter integer value in Age")
            continue
        else:
            if age <18:
                print("Age must be older then 18")
                continue
        data_entering = False
    
    data_entering = True
    while data_entering:
        try:
            salary = int(input("Enter Salary :"))
        except Exception:
            print("please enter integer value in Salary")
            continue
        else:
            if salary<1:
                print("Salary must be greater than 0")
                continue
        data_entering = False
    
    data_entering = True
    while data_entering:
        department = input("Enter Department :").strip().upper()
        if department == "":
            print("Department must not be emplty")
            continue
        data_entering = False

    skill = input("Enter skills :").strip().lower()

    data_entering = True
    while data_entering:
        dup = False
        email = input("Enter Email :").strip().lower()
        if email.count("@") != 1 or email.count(".com") != 1 :
            print("Invalid email id ")
            continue
        for k,v in d.items():
            if email == v["email"]:
                dup = True
        if dup == True:
            print("email already exist ")
            continue
        data_entering = False


    employee_dict[employee_id] = {
        "name" : name,
        "age" : age,
        "salary" : salary,
        "department" : department,
        "skill" : skill,
        "email" : email
    }
    print("Employee Added")
    return 



""" This function is for updating the data"""

@View_detail           #decorator is used here to view employee table
def update_emp():
    id = input("Enter Employee ID : ")
    try:
        if id in employee_dict:
            print("""
                1. Salary
                2. Department
                3. skills
                4. Email

            """)

            choice = int(input("Enter your Choice"))
            if choice == 1 :
                new_salary = int(input("Enter new salary : "))
                employee_dict[id]["salary"] = new_salary
            elif choice == 2:
                new_department = input("Enter New Department : ").strip().upper()
                employee_dict[id]["department"] = new_department
            elif choice ==3:
                new_skills = input("Enter new Skills : ")
                employee_dict[id]["skill"] = new_skills
            elif choice ==4:
                while True:
                    new_email = input("Enter new Email : ")
                    if "@" in new_email:
                        employee_dict[id]["email"] = new_email
                        break
                    else:
                        print("Please enter correct email")
            else:
                print("please choose correct option")

            print("Employee updated successfully.")
        else:
            print("Employee not Found")
    except ValueError:
        print(" Entered wrong input")
    except Exception:
        print("Try again")


"""This function is to delete data"""

@View_detail    # this decorator will add view employee feature
def del_emp():
    id = input("enter Employee id : ")
    if id in employee_dict:
        confirmation = input("Are you sure? (Y/N) : ").strip().lower()
        if confirmation == "y":
            employee_dict.pop(id)
            print("Employee deleted sucessfully")
    else:
        print("employee not found")





"""This function is to sort employee using lambda function """



def sort_emp():
    print("""
        Sort by :

        1. Name
        2. Salary
        3. Age
        4. Department
    
    """)
    try:
        choice = int(input("enter choice : "))

        if choice == 1:
            key = []
            data = []
            names = [x["name"] for x in employee_dict.values()]

            sorted_v = sorted(names, key = lambda x : x)
            for i in sorted_v:
                for k,v in employee_dict.items():
                    if v["name"] == i:
                        key.append(k)
                        data.append(v)
            employee_dict.clear()
            for i in range(len(key)):
                employee_dict[key[i]] = data[i]
        elif choice == 2:
            key = []
            data = []
            names = [x["salary"] for x in employee_dict.values()]

            sorted_v = sorted(names, key = lambda x : x)
            for i in sorted_v:
                for k,v in employee_dict.items():
                    if v["salary"] == i:
                        key.append(k)
                        data.append(v)
            employee_dict.clear()
            for i in range(len(key)):
                employee_dict[key[i]] = data[i]
        elif choice ==3:
            key = []
            data = []
            names = [x["age"] for x in employee_dict.values()]

            sorted_v = sorted(names, key = lambda x : x)
            for i in sorted_v:
                for k,v in employee_dict.items():
                    if v["age"] == i:
                        key.append(k)
                        data.append(v)
            employee_dict.clear()
            for i in range(len(key)):
                employee_dict[key[i]] = data[i]
        elif choice == 4:
            key = []
            data = []
            names = [x["department"] for x in employee_dict.values()]

            sorted_v = sorted(names, key = lambda x : x)
            for i in sorted_v:
                for k,v in employee_dict.items():
                    if v["department"] == i:
                        key.append(k)
                        data.append(v)
            employee_dict.clear()
            for i in range(len(key)):
                employee_dict[key[i]] = data[i]
        else:
            print("enter valid input")
        print("sorted sucessfully")
    
    except ValueError:
        print("Entered wrong value (please enter numeric value)")
    except Exception:
        print("Try Again")


""" This function is to save the data """

def save_data():
    try:
        if employee_dict != {}:
            print("Saving employee data...")
            load_data()
            with open("Data.txt","w") as file:
                for k,v in employee_dict.items():
                    s = f"{k}     {v}\n"
                    file.write(s)
    except Exception:
        print("data not saved")
    else:
        print("Data Saved Sucessfully")



""" This function is to load data """

def load_data():
    try:
        print("Loading employee data...")
        data = []
        with open("Data.txt","r") as f:
            for i in f:
                data = i.split("     ")
                if data[0] not in employee_dict:
                    employee_dict[data[0]] = eval(data[1]) # I have used eval() to convert string of dict to dict     #### but i can also use ast.literal_eval()   
    except FileNotFoundError:
        print("Data do not exist")
    except Exception:
        print("error occured")
    else:
        print("Employee loaded sucessfully.")


