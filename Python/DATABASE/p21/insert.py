import connection as con
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
