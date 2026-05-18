# Enterprise Management System

from Utilities import addcustomer,viewcustomer,deleteCustomer,addProduct,ViewProduct,updatePrice,PlaceAnOrder,viewOrders,viewOrderByCID



while True:
    print('n\t\t*** SARA ENTERPRISES ***')

    print('''
                1. Add Customer
                2. View all Customer
                3. Delete A Customer
                4. Add Product
                5. View All Product
                6. Update the Product Price
                7. Place An Order
                8. View All Orders
                9. View Orders By CID
                0. Exit
        ''')
    ch=int(input("n/t/tEnter your Choice : "))
    if ch==0:
        print("n\t\t Bye Bye Admin!")
        break
    elif ch==1:
        addcustomer()
        input("\t\t Press Enter to Continue..")
    elif ch==2:
        viewcustomer()  
        input("\t\t Press Enter to Continue..") 
    elif ch==3:
        deleteCustomer()
        input("\t\t Press Enter to Continue..")
    elif ch==4:
        addProduct()
        input("\t\t Press Enter to Continue..")
    elif ch==5:
        ViewProduct()
        input("\t\t Press Enter to Continue..")
    elif ch==6:
        updatePrice()
        input("\t\t Press Enter to Continue..")
    elif ch==7:
        PlaceAnOrder()
        input("\t\t Press Enter to Continue..")
    elif ch==8:
        viewOrders()
        input("\t\t Press Enter to Continue..")
    elif ch==9:
        viewOrderByCID()
        input("\t\t Press Enter to Continue..")



    
    

   





    



       



