import datetime
import mysql.connector as a
con=a.connect(host="localhost",user="root",
              password="1st@sql",database="project")
myc=con.cursor()
              
print("""     *~*~*~VINI BAKERS~*~*~*

1. STOCK MANAGEMENT
2. BILLING MANAGEMENT
  """)
choice=input("ENTER S.NO OF REQUIRED PROCESS: ")
print("")
while choice=='1':
    print(""" ~ ~ ~ WELCOME TO STOCK MANAGEMENT ~ ~ ~

    (1)   Add an item
    (2)  Modify an item
    (3) Delete an item """)
    step=int(input(" ENTER INDEX OF REQUIRED PROCESS: "))

    if step==1:
        Name=input("Enter Item Name: ")
        Code=int(input("Enter Item Code: "))
        Rate=int(input("Enter Item Rate: "))
        Stock=int(input("Enter Stock: "))

        query="insert into stock(Name,Code,Rate,Stock)values(%s,%s,%s,%s)"
        values=Name,Code,Rate,Stock
        myc.execute(query,values)
        print(Name,"is added successfully...")
        con.commit()
        print("")
        choice=input("ENTER S.NO OF REQUIRED PROCESS: ")
        print("")
    elif step==2:
        upd=int(input("Enter Item Code: "))
        Rate=int(input("Enter New Rate: "))
        Stock=int(input("Enter New Stock: "))
        query="update stock set Rate= '{}', Stock='{}' where Code= '{}' ".format(Rate,Stock,upd)
        myc.execute(query)
        print(upd, "is updated successfully...")
        con.commit()
        print("")
        choice=input("ENTER INDEX OF REQUIRED PROCESS: ")
        print("")
    elif step==3:
        delete=int(input("Enter Item Code: "))
        query="delete from stock where Code='{}'".format(delete)
        myc.execute(query)
        print(delete, " deleted successfully...")
        con.commit()
        print("")
        choice=input("ENTER S.NO OF REQUIRED PROCESS: ")
        print("")
while choice=='2':
    print(" * * * * WELCOME TO BILLING CENTRE * * * *")
    print("")
    num=int(input("Enter Bill Number: "))
    if num==0:
        print("")
        print(" # # # DAY COMPLETED # # # ")
        break
    else:
        code=int(input("Enter Product Code: "))
        rate=int(input("Enter Product Rate: "))
        qty=int(input("Enter Product Quantity: "))
        Amount=000

        now=datetime.datetime.now()
        Bill_date=now.strftime("%y-%m-%d")
        Bill_time=now.strftime("%H:%M:%S")
        query="""insert into bill(Bill_no,Code,Quantity,Amount,Bill_date,Bill_time)values(%s,%s,%s,%s,%s,%s)"""
        values=num,code,qty,Amount,Bill_date,Bill_time
        myc.execute(query,values)

        query="""update stock set stock=stock-'{}' where code='{}'""".format(qty,code)
        myc.execute(query)
        query="""update bill set amount='{}'*'{}' where Bill_no='{}'""".format(rate,qty,num)
        myc.execute(query)
        con.commit()
        print("=======================================================")
        print("")
        break
else:
    print(" * * * DAY COMPLETED * * *")
