"""
STUDENT MANAGEMENT SYSTEM
Student(sid,sname,sadd,source)

1. Add Student
2. View All Students
3. Delete Student
4. Update Student Info
0. Exit
"""
# Importing Modules/Library
import Utilities

# Data Storage
student = dict()

# Dashboard
while True:
    print("n\t\tStudent Management System")
    print('''
            1. Add Student
            2. View All Students
            3. Delete Student
            4. Update Student Info
            0. Exit
    ''')
    ch=int(input("\n\tEnter your Choice : "))
    if ch==0:
        print("\n\t\tBYE BYE ADMIN")
        break
    elif ch==1:
        student= Utilities.addstudent(student)
        print("\n\t\tstudent Added Successfully!")
        input("t\t Press Enter To Continue...")
    elif ch==2:
        Utilities.viewAllStudent(student)
        print("\n\t\tHere is your all Students...")
        input("\t\tPress Enter To Continue...")
    elif ch==3:
        Utilities.deleteStudent(student)
        input("\t\tPress Enter to Continue...")
    elif ch==4:
        student=Utilities.updateStudent(student)
        input("\t\tPress Enter to Continue...")
    else:
        print("\n\t\tWrong Entered\n\t\t Try Again!")

