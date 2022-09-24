import connection as con
q=con.mycon.cursor()
fetch="SELECT * FROM tbl_book"
try:
    q.execute(fetch)
    data=q.fetchall()
    for i in data:
        print(i)
except:
    print("No Data")
