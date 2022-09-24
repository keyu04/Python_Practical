import connection as con
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
finally:
    con.mycon.close()
