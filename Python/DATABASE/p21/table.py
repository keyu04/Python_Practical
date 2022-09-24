import connection as con
q=con.mycon.cursor()
v=q.execute("CREATE TABLE tbl_book(bid int auto_increment primary key,bname varchar(20),bpage int(3))")
if(v!=""):
    print("Created....")
else:
    print("Not Created....")
