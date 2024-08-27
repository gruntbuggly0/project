#from replit import db
#import sqlite3  # Import sqlite3 for SQLite

# Connect to PostgreSQL using DATABASE_URL
#cnctr = sqlite3.connect('cms.db')
#c = cnctr.cursor()
import datetime
import mysql.connector as sql
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
cnctr= sql.connect(host='localhost',user='root',passwd='1234',database='cms')
if cnctr.is_connected():
    print("connected to database")
c=cnctr.cursor()

# For table format in displaying data ----------------------------------------
def table(df):
    # Calculate widths of columns
    col_widths = [max(len(str(val)) for val in df[col]) for col in df.columns]
    col_widths = [max(width, len(col)) for col, width in zip(df.columns, col_widths)]

    # Print column headers with borders
    header = ' | '.join(f'{col:{width}}' for col, width in zip(df.columns, col_widths))
    border = '+-' + '-+-'.join('-' * width for width in col_widths) + '-+'

    print(border)
    print(f'| {header} |')
    print(border)

    # Print rows with borders
    for row in df.itertuples(index=False):
        row_str = ' | '.join(f'{str(val):{width}}' for val, width in zip(row, col_widths))
        print(f'| {row_str} |')
    print(border)
#-----------------------------------------------------------------------------

current_time = datetime.datetime.now()
x=1
while x==1:
    print("----NAVY CANTEEN MANAGEMENT SYSTEM----")
    print ("Welcome! Select one of the options if you are :\n1. A customer \n2. An Employee \n3. A Manager\n\n")


    try:
        choice= int(input("Enter your selection: ") )
    except ValueError:
        print("enter only integers. try again ")
        continue
    #when customer is selected-

    if choice == 1:
        print("\n\nWelcome customer! Select Action-\n 1. View your stored data\n 2. View Membership Status \n 3. Make a Purchase \n 4. New Customer \n 5. Back to Main menu")
        try:
            cr=int(input("\nenter your choice: "))
        except ValueError:
            print("enter only integers. try again ")
            continue
        #all choices inside customer-

        if cr==1:
            cid=int(input("Enter your customer ID : "))
            qry="select * from customer_data where C_ID=%s"
            c.execute(qry,(cid,))
            qres=c.fetchall()
            columns=[i[0] for i in c.description]
            df=pd.DataFrame(qres, columns=columns)
            print("\nCustomer stored data:\n")
            table(df)
            c.close()
            x=0

        elif cr==2:
            cid=int(input("Enter customer ID: "))
            qry='select MembershipType from customer_data where C_ID=%s'
            c.execute(qry,(cid,))
            qres=c.fetchall()
            if not qres:
                print("No data found. Try again.")
                continue
            else:
                print("Membership Status:", qres[0][0])
                c.close()
                x=0

        elif cr==3:
            cid=int(input("Enter your customer ID : "))
            qry='select Firstname from customer_data where C_ID=%s'
            c.execute(qry,(cid,))
            qres=c.fetchall()
            print("\n Select product category:\n")
            qry='select distinct category from Products'
            c.execute(qry)
            p=c.fetchall()
            for i in p:
                print(i[0],"\n")
            cgr=input("\nEnter category name in exact characters: ")
            print("\nSelect products from list below-")
            print("\nP_ID\t\tPRODUCT NAME\t\tPRICE\t\tEXPIRY DATE")
            qr='select pid,product, price, expiry_date from Products where category=%s and                  stock="in stock"'
            c.execute(qr,(cgr,))
            m=c.fetchall()
            if not m:
                print("\n --No data found. Make sure to type category exactly. Starting again.--")
                continue
            else:
                n=0
                for i in m:
                    print( i[0],"\t",i[1],"\t",i[2],"\t",i[3], "\n")
                    prod_list=[]
                y=1
                while y==1: 
                    t=int(input("\nEnter ID of selected product, press 0 to stop selecting:"))
                    if t==0:
                        y=0
                    else:
                        prod_list.append(t)
            cshr=input("\nenter cashier name:")
            print("..generating bill..")
            print("\n\n------------------------BILL------------------------\n\t\tcanteen\n----------------------------------------------------")
            dt='select now()'
            c.execute(dt)
            date=c.fetchall()
            print("\nCashier Name:",cshr,"\tDateTime:",current_time)
            print("\nCustomer Name:",qres[0][0])
            print("\n\nProduct\t\t\t\tPrice")
            print("------------------------\t--------------------")
            for i in prod_list:
                fb='select product,price from Products where pid=%s'
                c.execute(fb,(i,))
                prodtxt=c.fetchall()
                print(prodtxt[0][0],"\t",prodtxt[0][1],"\n")
            print("------------------------\t--------------------")
            price=[]
            for i in prod_list:
                fb = 'select price FROM Products WHERE pid=%s'
                c.execute(fb,(i,))
                spr=c.fetchone()
                price.append(spr[0])
            fbv=sum(price)
            fbv=float(fbv)
            print("TOTAL:\t\t\t\t",fbv)
            disc='select MembershipType from customer_data where C_ID=%s'
            c.execute(disc,(cid,))
            egb=c.fetchall()
            if egb[0][0]=="Premium":
                pd=fbv-(20/100)*fbv
                gst=pd+(5/100)*pd
                print("After premium discount:\t\t",pd)
                print("Final total with GST:\t\t",gst)
            else:
                pd=fbv
                gst=pd+(5/100)*pd
                print("Final total with GST:\t\t",gst)
            fp='update customer_data set last_purchase=%s where C_ID=%s'
            c.execute(fp,(gst,cid))
            cnctr.commit()
            dtlp='update customer_data set dateoflastpurchase=date(now()) where C_ID=%s'
            c.execute(dtlp,(cid,))
            cnctr.commit()
            print("\n\t\tOK SEE YOU")
            print("----------------------------------------------------")
            cnctr.close()
            x=0

        elif cr==4:
            cid=int(input("enter given customer ID: "))
            fn=input("Enter first name: ")
            ln=input("enter last name: ")
            email=input("enter email: ")
            phn=int(input("enter phone no.: "))
            mbr=input("enter membership type(premium/standard): ")
            newqr="insert into customer_data (C_ID,Firstname,Lastname,Email,PhoneNo,MembershipType) values (%s,%s,%s,%s,%s,%s)"
            c.execute(newqr,(cid,fn,ln,email,phn,mbr))
            cnctr.commit()
            print("---data stored successfully---")
            cnctr.close()
            x=0


        elif cr==5:
            print("\n\nGOING BACK TO MAIN MENU...\n\n")
            continue

        else:
            print("Enter valid integer. Try again")
            continue

    #when employee is selected-
    elif choice==2:
        print("Welcome Employee")
        eid=input("Enter your employee ID: ")
        pswd=input("Enter passwd to continue: ")
        eqr="select Passwd from employees where eID=%s"
        c.execute(eqr,(eid,))
        cpw=c.fetchall()
        if cpw[0]==pswd:
            ename="select Name from employees where Passwd=%s"
            c.execute(ename,(pswd,))
            en=c.fetchall()
            print("welcome",en[0])
            print("Select action- \n 1. View your data \n Change your password")
            echoice=input("Enter choice: ")
            if echoice==1:
                print("STORED DATA:")
                eqr="select * from employees where eID=%s"
                c.execute(eqr,(eid,))
                edata=c.fetchall()
                print("Name:",edata[0][0])
                print("eID:",edata[0][1])
                print("Passwd:",edata[0][2])
                print("Age:",edata[0][3])
                print("Salary:",edata[0][4])
                print("Position:",edata[0][5])
                cnctr.close()
                x=0
            elif echoice==2:
                newpw=input("Enter new password:")
                npqr="update employees set Passwd=%s where eID=%s"
                c.execute(npqr,(newpw,eid))
                cnctr.commit()
                cnctr.close()
                print("---password updated successfully---")
            else:
                print("choose valid option")
                continue
        else:
            print("Wrong password, Access denied")
            cnctr.close()
            x=0

    #when manager is selected-
    elif choice==3:
        print("\n\nWelcome Manager! Select action-\n 1. View product database\n 2. View employee database\n 3. View customer database\n 4. Back to main menu")
        try:
            cr=int(input("\nEnter your choice: "))
        except ValueError:
            print("enter only integers. try again.")

        if cr==1:
            qry="select * from products"
            c.execute(qry,)
            qres=c.fetchall()
            columns=[i[0] for i in c.description]
            df=pd.DataFrame(qres, columns=columns)
            print("\nProduct Database:\n")
            table(df)
            c.close()
            x=0

        elif cr==2:
            qry="select * from employees"
            c.execute(qry,)
            qres=c.fetchall()
            columns=[i[0] for i in c.description]
            df=pd.DataFrame(qres, columns=columns)
            print("\nEmployee Database:\n")
            table(df)
            c.close()
            x=0

        elif cr==3:
            qry="select * from customer_data"
            c.execute(qry,)
            qres=c.fetchall()
            columns=[i[0] for i in c.description]
            df=pd.DataFrame(qres, columns=columns)
            print("\nCustomer Database\n")
            table(df)
            c.close()
            x=0

        elif cr==4:
            print("\n\nGOING BACK TO MAIN MENU...\n\n")
            continue

        else:
            print("Enter valid integer. Try again")
            continue
