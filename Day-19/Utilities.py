
# Importing Required Libraries
import pickle

def addcustomer():
    file=open("Customer.bin","ab")
    cid=input("n\t\t Enter Customer ID : ")
    cname=input("n\t\t Enter Customer Name : ")
    cadd=input("n\t\t Enter Customer Address : ")
    cmob=input("Enter Customer Mobile : ")
    cus=[cid,cname,cadd,cmob]
    pickle.dump(cus,file)
    file.close()
    print("n\t\t Customer Added Successfully!")

def viewcustomer():
    file=open("Customer.bin","rb")
    try:
        while True:
            data=pickle.load(file)
            print("n\t\tCustomer ID :",data[0])
            print("n\t\tCustomer Name :",data[1])
            print("n\t\tCustomer Address :",data[2])
            print("n\t\tCustomer Mobile :",data[3])
            print("t\t---------------------------")
    except:
        print("\n\t\t Here is your all Customers..")
    file.close()

def deleteCustomer():
    file=open("Customer.bin","rb")
    customers=[]
    flag=0
    cid=input("n\t\t Enter Customer ID To Delete :")
    try:
        while True:
            data=pickle.load(file)
            if data[0]!=cid:
                customers.append(data)
            else:
                flag=1  
    except:
        pass
    file.close()
    file=open("Customer.bin",'wb')
    for cus in customers:
        pickle.dump(cus,file)
    file.close()
    if flag==1:
        print("n\t\tCustomer Deleted Successfully!")
    else:
        print("n\t\t Customer Not Found!")

def addProduct():

    file = open("product.bin", "ab")
    pid = input("\n\t\t Enter Product ID : ")
    pname = input("\t\t Enter Product Name : ")
    price = input("\t\t Enter Product Price : ")
    pdesc = input("\t\t Enter Product Desc : ")
    data = {pid:[pname, price, pdesc]}
    pickle.dump(data, file)
    file.close()
    print("\n\t\t Product Added Successfully!")

def ViewProduct():
    file=open("product.bin","rb")
    try:
        while True:
                product=pickle.load(file)
                for pid,data in product.items():
                    print("\n\t\tProduct ID : ",pid)
                    print("\t\tProduct Name : ",data[0])
                    print("\t\tProduct Price : ",data[1])
                    print("\t\tProduct Desc : ",data[2])
                    print("\t\t-------------------------")
    except:
        print("\n\t\tHere is all your Products!")

    file.close()


def updatePrice():
    file=open("product.bin","rb")
    pid=input("\n\t\tEnter Product ID : ")
    pro=[]
    flag=0
    try:
        while True:
            data=pickle.load(file)
            if list(data.keys())[0]==pid:
                for p_id,p_data in data.items():
                    print("\t\tProduct Name : ",p_data[0])
                    print("\t\tProduct Old Price : ",p_data[1])
                    print("\t\tProduct Desc : ",p_data[2])
                    price=input("\t\tEnter New Price : ")
                    pro.append({p_id:[data[0],price,data[2]]})
                    flag=1
            else:
                pro.append(data)
    
    except:
        pass
    file.close()
    file=open("product.bin","wb")
    for item in pro:
        pickle.dump(item,file)
    file.close()
    if flag==1:
        print("\n\t\tProduct Updated Successfully !")
    else:
        print("n\t\tProduct Not Found This ID !")

def getCustomer(cid):
    file=open("customer.bin","rb")
    flag=False
    try:
        while True:
            data=pickle.load(file)
            if data[0]==cid:
                  flag=data
                 
    except:
        pass
    file.close()
    return flag

def getProduct(pid):
    file=open("product.bin","rb")
    flag=False
    try:
        while True:
            data=pickle.load(file)
            if list(data.keys())[0]==pid:
                flag=data
    except:
        pass
    file.close()
    return flag

def PlaceAnOrder():
    cid=input("n\t\t Enter Customer ID : ")
    cus=getCustomer(cid)
    if cus:
        print("\t\tCustomer Name :","cus[1]")
        print("\t\tCustomer Add :","cus[2]")
        pid=input("\t\t Enter Product ID :")
        pro=getProduct(pid)
        if pro:
            data=pro.get(pid)
            print("\t\tProduct Name :",data[0])
            print("\t\tProduct Price :",data[1])
            print("\t\tProduct Desc :",data[2])
            qty=input("\t\tEnter Quantity : ")
            print("\n\t\tTotal Bill : ",float(data[1])*int(qty))
            file=open("orders.bin","ab")
            data=[cid,pid,qty]
            pickle.dump(data,file)
            print("\n\t\t Order Placed Successfully !")
        else:
            print("\t\tProduct Not Found !")

            
    else:
             print("\t\tProduct Not Found !")
def viewOrders():
    file=open("orders.bin","rb")
    order_id=1001
    try:
        while True:
            data=pickle.load(file)
            cus=getCustomer(data[0])
            pro=getProduct(data[1]).get(data[1])
            qty=int(data[2])
            print("\n\t\tOrder No.",order_id)
            print("\t\t Customer Name :",cus[1])
            print("\t\tCustomer Address :",cus[2])
            print("\t\tCustomer Mobile :",cus[3])
            print("\t\tProduct Name :",pro[0])
            print("\t\tProduct Price:",pro[1])
            print("\t\tProduct Desc :",pro[2])
            print("\t\tProduct Quantity :",qty)
            print("\t\tTotal Bill :",float(pro[1])*qty)
            order_id+=1
            print("t\t---------------------------------")
      
    except:
        print("\n\t\tHere is your all Orders !")
    file.close()

def viewOrderByCID():
    file=open("orders.bin","rb")
    order_id=1001
    cid=input("\n\t\tEnter Customer ID : ")
    try:
        while True:
            data=pickle.load(file)
            cus=getCustomer(data[0])
            pro=getProduct(data[1]).get(data[1])
            qty=int(data[2])
            if cus[0]==cid:

                print("\n\t\tOrder No.",order_id)
                print("\t\t Customer Name :",cus[1])
                print("\t\tCustomer Address :",cus[2])
                print("\t\tCustomer Mobile :",cus[3])
                print("\t\tProduct Name :",pro[0])
                print("\t\tProduct Price:",pro[1])
                print("\t\tProduct Desc :",pro[2])
                print("\t\tProduct Quantity :",qty)
                print("\t\tTotal Bill :",float(pro[1])*qty)
                order_id+=1
                print("t\t---------------------------------")
    except:
        print("\n\t\tHere is your all Orders !")
    file.close()


            
       


    


        
        
        
        





