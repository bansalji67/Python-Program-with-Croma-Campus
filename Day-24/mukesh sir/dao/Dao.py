from utils.Connection import DBConnect

class EmployeeDao:
    def addEmployee(emp):
        sql = "insert into employee(ename,eadd,esal) value(%s,%s,%s)"
        data = (emp.ename , emp.eadd , emp.esal )
        conn = DBConnect.getConnection()
        cur = conn.cursor()
        cur.execute(sql,data)
        if cur.rowcount>0:
            print("Employee Added")
        else:
            print("Employee Add Failed!")
        conn.commit()
        cur.close()
        conn.close() 

    def viewEmployee():
        with DBConnect.getConnection() as conn:
            cur = conn.cursor()
            sql = "SELECT * FROM employee"
            cur.execute(sql) 
            data = cur.fetchall()
            for emp in data:
                print("EmpID    \t:",emp[0])
                print("EmpName    \t:",emp[1])
                print("EmpAdd    \t:",emp[2])
                print("EmpSal    \t:",emp[3])
                print("-------------------------")
            cur.close()
