import sqlite3
values=[(5,"e"),(6,"f")]
con=sqlite3.connect('db1')
# con.execute('CREATE TABLE mytable(id int(20),name varchar(20),PRIMARY KEY(id));')
# con.execute('CREATE TABLE MYTABLE(idint(20),name char(20));')
# con.executemany('INSERT INTO mytable VALUES(?,?)',values)
con.execute('delete from mytable where id=9')
con.execute('insert into mytable values(9,"i")')
con.execute('update mytable set name="iii" where id=9')

rs=con.execute('SELECT * FROM mytable')
for i in rs:
    print i
    print i[0],i[1]
con.commit()