# Employee Management System
from utils.Entity import Employee
from dao.Dao import EmployeeDao

while True:
    print('''
        1. Add Employee
        2. View Employee
        0. Exit
          ''')
    ch = int(input("Enter Your Choice : "))
    if ch==0:
        print("Bye-Bye Admin!")
        break
    elif ch==1:
        ename = input("Enter Employee Name : ")
        eadd = input("Enter Employee Address : ")
        esal = input("Enter Employee Salary : ")
        emp = Employee(ename,eadd,esal)
        EmployeeDao.addEmployee(emp)
        input("\n\tPress Enter To Continue...")
    elif ch==2:
        EmployeeDao.viewEmployee()
        input("\n\tPress Enter To Continue...")