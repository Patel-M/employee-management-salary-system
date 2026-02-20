import mysql.connector
def Employee_master():
    print("---------------------------")
    print("Employee Salary Management System")
    print("---------------------------")
    d={1:"Employee Detail Management",
       2:"Employee Salary Management",
       'OTHERS':"EXIT"}  
    for i,j in d.items():
       print(i,":",j)
    c=int(input("Enter your choice:"))
    if c==1:
        emp_master()
    elif c==2:
        emp_salary()
    else:
        print("Wrong choice")
        print("Thank you for using this project")
def emp_master():
    print("-------------------------")
    print("Employee Detail Management")
    print("-------------------------")
    d={1:"Enter new Employee details",
       2:"Modify current Employee details",
       3:"Delete current Employee details",
       4:"Display all Employee details",
       5:"Search specific Employee details",
       'OTHERS':"BACK TO MAIN MENU"}
    for i,j in d.items():
        print(i,":",j)
    c=int(input("Enter your choice:"))
    if c==1:
        Emp_insert()
    elif c==2:
        Emp_modify()
    elif c==3:
        Emp_delete()
    elif c==4:
        Emp_display()
    elif c==5:
        Emp_search()
    else:
        print("Invalid choice")
        Employee_master()
def Emp_insert():
    eno=int(input("Enter Employee number:"))
    mycursor.execute("select * from employee;")
    for x in mycursor:
        pass
    if mycursor.rowcount==-1:
        name=input("Enter Employee name:")
        address=input("Enter Employee address:")
        contact=input("Enter Employee contact number:")
        des=input("Enter Employee designation:")
        query="insert into employee values('%d','%s','%s','%s','%s');"%(eno,name,address,contact,des)
        mycursor.execute(query)
        db.commit()
        print(mycursor.rowcount,"record inserted")
    else:
        mycursor.execute("select * from employee where eno='%d';"%(eno))
        for x in mycursor:
            pass
        if mycursor.rowcount==1:
            print("Entered Employee number is already exists")
        else:
            name=input("Enter Employee name:")
            address=input("Enter Employee address:")
            contact=input("Enter Employee contact number:")
            des=input("Enter Employee designation:")
            query="insert into employee values('%d','%s','%s','%s','%s');"%(eno,name,address,contact,des)
            mycursor.execute(query)
            db.commit()
            print(mycursor.rowcount,"record inserted")
    emp_master()
def Emp_modify():
    mycursor.execute("select * from employee;")
    for x in mycursor:
        pass
    if mycursor.rowcount==-1:
        print("No records present to modify")
    else:
        eno=int(input("Enter employee number:"))
        mycursor.execute("select * from employee where eno='%d';"%(eno))
        for x in mycursor:
            pass
        if mycursor.rowcount==-1:
            print("Entered Employee number is not present to modify")
        else:
            name=input("Enter Employee name:")
            address=input("Enter Employee address:")
            contact=input("Enter Employee contact number:")
            des=input("Enter Employee designation:")
            query="update employee set e_name='%s',e_address='%s',e_contact='%s', e_des='%s' where eno='%d';"%(name,address,contact,des,eno)
            mycursor.execute(query)
            db.commit() 
            print(mycursor.rowcount,"record updated")
    emp_master()
def Emp_delete():
    mycursor.execute("select * from employee;")
    for x in mycursor:
        pass
    if mycursor.rowcount==-1:
        print("No records present to delete")
    else:
        eno=int(input("Enter Employee number:"))
        mycursor.execute("select * from employee where eno='%d';"%(eno))
        for x in mycursor:
            pass
        if mycursor.rowcount==-1:
            print("Entered Employee number is not present to delete")
        else:
            query="delete from employee where eno='%d';"%(eno)
            mycursor.execute(query)
            db.commit() 
            print(mycursor.rowcount,"record deleted")
    emp_master()
def Emp_display():
    mycursor.execute("select * from employee;")
    for x in mycursor:
        print(x)
    if mycursor.rowcount==-1:
        print("No records to display")
    else:
        print(mycursor.rowcount,"rows in set")
    emp_master()
def Emp_search():
    eno=int(input("Enter Employee number:"))
    mycursor.execute("select * from Employee where eno='%d';"%(eno))
    for x in mycursor:
        print(x)
    if mycursor.rowcount==-1:
        print("Entered Employee number is not present")
    else:
        print(mycursor.rowcount,"rows in set")
    emp_master()
def emp_salary():
    print("-------------------------")
    print("Transaction Management")
    print("-------------------------")
    d={1:"Enter employee salary detail",
       2:"Display monthwise salary statement",
       3:"Display employee salary statement",
       'OTHERS':"BACK TO MAIN MENU"}
    for i,j in d.items():
        print(i,":",j)
    c=int(input("Enter your choice:"))
    if c==1:
        salary_insert()
    elif c==2:
        salary_month()
    elif c==3:
        salary_emp()
    else:
        print("Invalid choice")
        Employee_master()
def salary_insert():
    eno=int(input("Enter Employee number:"))
    mycursor.execute("select * from Employee where eno='%d';"%(eno))
    for x in mycursor:
        print(x)
    if mycursor.rowcount==-1:
        print("Entered Employee number is not present. First insert emmployee detail")
    else:
        s_date=input("Enter salary date:")
        bs=int(input("Enter basic salary:"))
        da=bs*20/100
        hra=bs*25/100
        ma=bs*5/100
        pf=bs*12/100
        total=bs+da+hra+ma-pf
        query="insert into emp_salary values('%d','%s','%d','%d','%d','%d','%d','%d');"%(eno,s_date,bs,da,hra,ma,pf,total)
        mycursor.execute(query)
        db.commit()
        print(mycursor.rowcount,"record inserted")
    emp_salary()
def salary_month():
    month=input("Enter month")
    print()
    mycursor.execute("select * from emp_salary where month(s_date)='%s';"%(month))
    for x in mycursor:
        print(x)
    if mycursor.rowcount==-1:
        print("No records present for this month")
    emp_salary()
def salary_emp():
    eno=int(input("Enter Employee number"))
    print()
    mycursor.execute("select * from emp_salary where eno='%d';"%(eno))
    for x in mycursor:
        print(x)
    if mycursor.rowcount==-1:
        print("No records present for this empno")
    emp_salary()
db=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=db.cursor()
found='n'
mycursor.execute("show databases;")
for x in mycursor:
    if 'emp' in x:
        found='y'
if found=='n':
    mycursor.execute("create database emp;")
    mycursor.execute("use emp;")
    mycursor.execute("create table employee(eno int,\
                                    e_name varchar(20),\
                                    e_address varchar(20),\
                                    e_contact varchar(12),\
                                    e_des varchar(10));")
    mycursor.execute("create table emp_salary(eno int,\
                                    s_date date,\
                                    bs int,\
                                    da int,\
                                    hra int,\
                                    ma int,\
                                    pf int,\
                                    gs int);")
    
if found=='y':
    mycursor.execute("use emp;")
Employee_master()