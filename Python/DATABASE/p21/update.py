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
