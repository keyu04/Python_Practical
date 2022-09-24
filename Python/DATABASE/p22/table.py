import connection as con
q=con.mycon.cursor()
q.execute("create table tbl_registration(rid int auto_increment primary key,rname varchar(20),rphone int(10),clgname varchar(20) )")
