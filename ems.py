import C
import read
import string
import time 
import os


def main_menu():
    print("""
            EMPLOYEE MANAGEMENT SYSTEM
======================================================
    
    1.  Add  Employee
    2.  View Employee
    3.  Search Employee
    4.  Update Employee
    5.  Delete Employee
    6.  Sort Employee
    7.  Salary Report
    8.  Department Report
    9.  Skill Report
    10. Save Data
    11. Load Data
    12. Exit 
    """)



while True:
    os.system("cls")
    try:
        main_menu()
        time.sleep(1)
        input_data = int(input("Enter the choice : "))
    
    except Exception:
        print("enter integer value")
        time.sleep(210)
        main_menu()
    except KeyboardInterrupt:
        print("Returning to main menu")
        time.sleep(2)
    else:
        
        if input_data == 12:
            print("Thanks For using Employee Management System")
            break
        elif input_data == 1:
            C.Add_employee()
            time.sleep(1)
        elif input_data == 2:
            read.view()
            time.sleep(1)
        elif input_data == 3:
            read.search()
            time.sleep(1)
        elif input_data == 4:
            C.update_emp()
            time.sleep(1)
        elif input_data == 5:
            C.del_emp()
            time.sleep(1)
        elif input_data == 6:
            C.sort_emp()
            time.sleep(1)
        elif input_data == 7:
            read.salary_report()
            time.sleep(1)
        elif input_data == 8:
            read.depart_report()
            time.sleep(1)
        elif input_data == 9:
            read.skill_report()
            time.sleep(1)
        elif input_data == 10:
            C.save_data()
            time.sleep(1)
        elif input_data == 11:
            C.load_data()
            time.sleep(1)
        else:
            print("wrong input")
            time.sleep(2)
            




