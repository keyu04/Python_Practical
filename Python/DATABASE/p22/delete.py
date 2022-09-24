import connection as con
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
