import C
import read
import string


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
    12. Memory Demonstration
    13. Exit 
    """
)


while True:
    
    try:
        input_data = int(input("Enter the choice"))
    except Exception:
        print("enter integer value")
    else:
        if input_data == 13:
            break
        elif input_data == 1:
            C.Add_employee()
        elif input_data == 2:
            read.view()
        elif input_data == 3:
            read.search()
        elif input_data == 4:
            C.update_emp()
        elif input_data == 5:
            C.sort_emp()
        else:
            print("wrong input")
