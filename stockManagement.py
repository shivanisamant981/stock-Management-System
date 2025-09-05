#har har mahadev

#Stock management system
import os
import mysql.connector

def product_management():
    while True:
        
        print("\t\t\t 1: ADD NEW PRODUCT ")
        print("\t\t\t 2: lIST PRODUCT ")
        print("\t\t\t 3: UPDATE PRODUCT")
        print("\t\t\t 4: DELETE PRODUCT ")
        print("\t\t\t 5: BACK TO MAIN MENU ")
        n=int(input("Enter your choice"))
        if n==1:
            add_product()
        elif n==2:
            list_product()
        elif n==3:
            update_product()
        elif n==4:
            delete_poduct()
        elif n==5:
            break;
def purchase_management():
    while True:
        
        print("\t\t\t 1: ADD ORDER ")
        print("\t\t\t 2: lIST ORDER")
        print("\t\t\t 3: Back TO MAIN MENU")
        
       
        n=int(input("Enter your choice"))
        if n==1:
            add_order()
        elif n==2:
            list_order()
        elif n==3:
            break;
    
def Sales_management():
    while True:
        
        print("\t\t\t 1: Sale Items")
        print("\t\t\t 2: lIST SALES")
        print("\t\t\t 3: Back TO MAIN MENU")
        
       
        n=int(input("Enter your choice"))
        if n==1:
            sales_product()
        elif n==2:
            list_sales()
        elif n==3:
            break;
def user_management():
    while True:
        
        print("\t\t\t 1:ADD USER")
        print("\t\t\t 2: lIST USER")
        print("\t\t\t 3: Back TO MAIN MENU")
        
       
        n=int(input("Enter your choice"))
        if n==1:
            add_user()
        elif n==2:
            list_user()
        elif n==3:
            break;
        
def database_management():
    while True:
         print("\t\t\t 1:DATABASE CREATION")
         print("\t\t\t 2:LIST DATABASE")
         print("\t\t\t 3:Back to main MENU")
         n =int(input("ENTER YOUR CHOICE "))
         if n==1:
             create_database()
         elif n==2:
             list_database()
         elif n==3:
             break;

def create_database():
    mydb=mysql.connector.connect(host="localhost" ,user="root", passwd="743211",database="stock")
    mycursor=mydb.cursor()
    print("Creating product table")
    sql="CREATE TABLE if not exists prodcut (\
        pcode int (4) PRIMARY KEY,\
        pname char(30) NOT NULL,\
        pprice float(8,2),\
        pqty int(4),\
        pcat char(30));"
    mycursor.execute(sql)
        

        

 
while(True):
    os.system("cls")
    print("\t\t\t STOCK MANAGEMENT SYSTEM ")
    print("\t\t\t ***********************************\t")
    print("\t\t\t 1. PRODUCT MANAGEMENT ")
    print("\t\t\t 2. PURCHASE MANAGEMENT ")
    print("\t\t\t 3. SALES MANAGEMENT ")
    print("\t\t\t 4. USER MANAGEMENT ")
    print("\t\t\t 5. DATABASE SETUP ")
    print("\t\t\t 6. EXIT ")
    n=int(input("enter the number"))
    if n==1:
          product_management()
    elif n==2:
          purchase_management()
    elif n==3:
          sales_management()
    elif n==4:
         user_management()
    elif n==5:
          database_management()
    elif n==6:
        break;
    
          
        
        

