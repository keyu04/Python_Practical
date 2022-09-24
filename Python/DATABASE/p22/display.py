import connection as con
q=con.mycon.cursor()
sql="select * from tbl_registration"
try:
    q.execute(sql)
    data=q.fetchall()
    for i in data:
        print(i)
except:
    print("No Data Available...")
