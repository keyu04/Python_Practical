import connection as con
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
