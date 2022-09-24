import connection as con
def insert():
    bname=input("Enter BookName ")
    bpage=int(input("Enter Pages "))
    q=con.mycon.cursor()
    sql="INSERT INTO tbl_book(bname,bpage) VALUES (%s,%s)"
    val=(bname,bpage)
    try:
        v=q.execute(sql,val)
        con.mycon.commit()
        print("Data Inserted...")
    except:
        con.mycon.rollback()
        print("Data Not Inserted...")
    

def update():
    q=con.mycon.cursor()
    fetch="SELECT * FROM tbl_book"
    try:
        q.execute(fetch)
        data=q.fetchall()
        for i in data:
            print(i)
    except:
        print("No Data")
    print("")
    bid=int(input("Enter BookId to Book Detail "))
    sql="SELECT * FROM tbl_book where bid=%s"
    upval=(bid,)
    try:
        q.execute(sql,upval)
        data=q.fetchall()
        for i in data:
            bname=i[1]
            bpage=i[2]
        print("1. update bookname")
        print("2. update bookpages")
        ch=input("Enter choices ")
        if(ch=='1'):
            bname=input("Enter Bookname ")
        elif(ch=='2'):
            bpage=input("Enter Bookpage ")
        else:
            print("Invalid Input..")
        sql="update tbl_book set bname=%s,bpage=%s where bid=%s"
        val=(bname,bpage,bid)
        try:
            q.execute(sql,val)
            con.mycon.commit()
            print("Updated..")
        except:
            print("Not Updated..")
    except:
        print("No data available")
    
def delete():    
    bname=input("Enter BookName ")
    q=con.mycon.cursor()
    sql="DELETE FROM `tbl_book` WHERE bname=%s"
    val=(bname,)
    try:
        v=q.execute(sql,val)
        con.mycon.commit()
        print("Deleted...")
    except:
        con.mycon.rollback()
        print("Not Deleted...")
    
def select():
    q=con.mycon.cursor()
    fetch="SELECT * FROM tbl_book"
    try:
        q.execute(fetch)
        data=q.fetchall()
        for i in data:
            print(i)
    except:
        print("No Data")
   

n=0
while n!=5:
    print("")
    print("---Menu---")
    print("1.Insert")
    print("2.Update")
    print("3.Delete")
    print("4.Display")
    print("5.Exit")
    print("")
    ch=int(input("Enter Choice: "))
    if ch==1:
        insert()
    elif ch==2:
        update()
    elif ch==3:
        delete()
    elif ch==4:
        select()
    else:
        break
