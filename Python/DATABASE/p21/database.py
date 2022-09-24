import connection as c
my=c.mycon.cursor()
q=my.execute("CREATE DATABASE Address_Book")
if(q!=""):
    print("Created....")
else:
    print("Not Created....")

