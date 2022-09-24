import connection as con
def registration():    
    q=con.mycon.cursor()
    name=input("Enter Name ")
    phone=int(input("Enter Phone "))
    name=input("Enter CollageName ")
    data=(name,phone,name)
    sql="insert into tbl_registration(rname,rphone,clgname)values(%s,%s,%s)"
    try:
        q.execute(sql,data)
        con.mycon.commit()
        print("Registration Successfully Done...")
    except:
        con.mycon.rollback()
        print("Registration is Fail...")
def cancel():
    q=con.mycon.cursor()
    sql="select * from tbl_registration"
    try:
        q.execute(sql)
        data=q.fetchall()
        for i in data:
            print(i)
        rid=int(input("Enter Registration Id To Cancel Registration: "))
        val=(rid,)
        sql1="DELETE FROM tbl_registration where rid=%s"
        try:
            q.execute(sql1,val)
            con.mycon.commit()
            print("Cancel Registration...")
        except:
            con.mycon.rollback()
            print("Pendding To cancel Registration...")
    except:
        print("No Data Available")
def display():
    q=con.mycon.cursor()
    sql="select * from tbl_registration"
    try:
        q.execute(sql)
        data=q.fetchall()
        for i in data:
            print(i)
    except:
        print("No Data Available...")
n=0
while n!=4:
    print("")
    print("1.Event Registration")
    print("2.Cancel Registration")
    print("3.Display a record")
    print("4.Exit")
    print("")
    n=int(input("Enter Choice "))
    if n==1:
        registration()
    elif n==2:
        cancel()
    elif n==3:
        display()
    else:
        break
