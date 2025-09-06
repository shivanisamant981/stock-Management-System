#har har mahadev

#Stock management system
import datetime
now=datetime.datetime.now()

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
            delete_product()
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
    #product table
    print("Creating product table")
    sql="CREATE TABLE if not exists product (\
        pcode int (4) PRIMARY KEY,\
        pname char(30) NOT NULL,\
        pprice float(8,2),\
        pqty int(4),\
        pcat char(30));"
    mycursor.execute(sql)
    # order table
    print("Crating ORDER TABLE")
    sql="CREATE TABLE if not exists orders(\
    orderid int(4) PRIMARY KEY,\
    orderdate DATE,\
    pcode char(30) NOT NULL,\
    pprice float(8,2),\
    pqty int(4),\
    supplier char(30)); "
    mycursor.execute(sql)
    print("ORDER table created")
    
    #sales table
    
    sql="CREATE TABLE  if not exists sales(\
        salesid int(4) PRIMARY KEY,\
        salesdate DATE,\
        pcode int(4) references product(pcode),\
        pprice float(8,2),\
        pqty int(4),\
        total double(8,2));"
    mycursor.execute(sql)
    print("SALES table created")

    #user table
    sql="CREATE TABLE if not exists user(\
            uid char(6) PRIMARY KEY,\
            uname char(30) NOT NULL,\
            upwd char(30));"
    mycursor.execute(sql)
    print("USER table created")
    

def list_database():
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="743211" , database="stock")
    mycursor=mydb.cursor()
    sql="show tables"
    mycursor.execute(sql)
    for i in mycursor:
        print (i)


def add_order():
    mydb=mysql.connector.connect(host="localhost",user="root",password="743211",database="stock")
    mycursor=mydb.cursor()
    now=datetime.datetime.now()
    sql="INSERT INTO orders( orderid,orderdate ,pcode,pprice ,pqty ,supplier) value(%s,%s,%s,%s,%s,%s)"
    code=int (input("enter the product code:"))
    oid=now.year+now.month+now.day+now.hour+now.minute+now.second
    qty=int(input("enter product quantity"))
    price=float(input("Enter the product unit price"))
    supplier=input("Enter supplier details")
    val=(oid,now,code,price,qty,supplier)
    mycursor.execute(sql, val)
    mydb.commit()
def list_order():
    mydb=mysql.connector.connect(host="localhost", user="root", passwd="743211",database="stock")
    mycursor=mydb.cursor()
    sql="SELECT * from orders"
    mycursor.execute(sql)
    print("\t\t\t\t\t ORDER DETAILS")
    print("-"*85)
    for i in mycursor:
        print("orderID\t orderdate \t pcode \t pprice  \t pqty \t supplier")
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t",i[5])
    print("-"*85)
    
def add_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="743211",database="stock")
    mycursor=mydb.cursor()
    sql="INSERT INTO product(pcode , pname,pprice, pqty,pcat)values(%s,%s,%s,%s,%s)"
    code=int(input("\t\tEnter product code"))
    search="SELECT count(*) From product where pcode=%s;"
    val=(code,)
    mycursor.execute(search,val)
    for x in mycursor:
        cnt=x[0]
    if cnt==0:
        name=input("\t\tenter the product name")
        qty=int(input("Enter product quantity"))
        price=float(input("\t\tEnter product unit price"))
        cat=input("\t\t Enter product category")
        val=(code,name,price, qty, cat)
        mycursor.execute(sql, val)
        mydb.commit()
    else:
        print("\t\tProduct already exist")
        
def list_product():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="743211",database="stock")
    mycursor=mydb.cursor()
    sql="SELECT * FROM PRODUCT"
    mycursor.execute(sql)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*47)
    print("\t\t code name price quantity category")
    print("\t\t","-"*47)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
    print("\t\t","-"*47)

def update_product():
    mydb=mysql.connector.connect(host="localhost",user="root", passwd="743211", database="stock")
    mycursor=mydb.cursor()
    code=int(input("enter the code"))
    qty=int(input("enter the quantity"))
    sql="UPDATE product SET pqty=pqty+%s WHERE  pcode=%s;"
    val=(qty,code)
    mycursor.execute(sql, val)
    mydb.commit()
    print("\t\t Product details update")

def delete_product():
    mydb=mysql.connector.connect(host="localhost",user="root", passwd="743211", database="stock")
    mycursor=mydb.cursor()
    code=int(input("ENTER the prodcut code"))
    sql="DELETE from product where pcode=%s;"
    val=(code,)
    mycursor.execute(sql, val)
    mydb.commit()
    
def add_user():
    mydb=mysql.connector.connect(host="localhost",user="root", passwd="743211", database="stock")
    mycursor=mydb.cursor()
    userid=int(input("Enter the userid"))
    username=input("Enter the name")
    userpwd=int(input("Enter the password"))
    sql="INSERT INTO user values(%s,%s,%s);"
    val=(userid, username,userpwd)
    mycursor.execute(sql, val)
    mydb.commit()

def list_user():
    mydb=mysql.connector.connect(host="localhost",user="root", passwd="743211", database="stock")
    mycursor=mydb.cursor()
    sql="Select * from user";
    mycursor.execute(sql);
    print("\t\t\t","-"*40 )
    print("-"*30,"user DETAILS")
    print("\t userid \t\t username \t\t userpwd")
    for i in mycursor:
        print(i[0],"\t\t",i[1],"\t\t",i[2]);
    print("\t\t\t","-"*40)

    
    
        

 
while(True):
    
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
    
          
        
        

