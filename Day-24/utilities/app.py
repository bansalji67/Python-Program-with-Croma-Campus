# Employee Management System
from utilities.Entity import Employee 

while True:
    print('''
        1. Add Employee
        2. View Employee   
        ''')
    ch=int(input("Enter Your Choice : "))
    if ch==1:
        ename = input("Enter Employee Name : ")
        eadd  = input("Enter Employee Address : ")
        esal  = input("Enter Employee Salary : ")

        