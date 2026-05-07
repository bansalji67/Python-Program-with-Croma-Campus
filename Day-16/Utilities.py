def addstudent(student):
    sid=input("\n\t\tEnter Student ID: ")
    sname=input("\t\tEnter Student Name: ")
    sadd=input("\t\tEnter Student Address: ")
    scourse=input("\t\tEnter Student Course: ")
    student.update({sid:[sname,sadd,scourse]})
    return student

def viewAllStudent(student):
    for sid,data in student.items():
        print("\n\t\tStudent ID :",sid)
        print("\t\tStudent Name :",data[0])
        print("\t\tStudent Address :",data[1])
        print("\t\tStudent Course :",data[2])
        print("t\t--------------------------")

def deleteStudent(student):
    sid  = input("\n\t\tEnter Student ID To Delete! ")
    data = student.get(sid,"\n\t\t Student Not Found!")
    if type(data)==list:
        print("\t\tStudent Name :",data[0])
        student.pop(sid)
        print("\t\tStudent Delete Successfully!")
    else:
        print(data)
        return student
def updateStudent(student):
    sid=input("\n\t\tEnter Student ID to Update")
    data=student.get(sid,"\t\tStudent not Found!")
    if type(data)==list:
        print("\t\tStudent Name :",data[0])
        print("\t\tStudent Old Address",data[1])
        add=input("\t\tEnter New Address: ")
        print("\t\tStudent Old Course : ",data[2])
        course=input("\t\tEnter New Course: ")
        student.update({sid:[data[0],add,course]})
        print("\t\tStudent Updated Successfully")
    else:
        print(data)
    return student
