import pymysql
db=pymysql.connect('localhost','root','root')
cur=db.cursor()
cur.execute('use sampledb')
# p1id=raw_input('enter id of p1:')
# p1name=raw_input('enter name of p1:')
# p2id=raw_input('enter id of p2:')
# p2age=raw_input('enter age of p2:')
# cur.execute('insert into person1 values(%s,%s)',(p1id,p1name))
# cur.execute('insert into person2 values(%s,%s)',(p2id,p2age))
# cur.execute('select * from person1')
# rs=cur.fetchall()
# for i in rs:
#     print i[0],i[1]
# cur.execute('select * from person2')
# rs=cur.fetchall()
# for i in rs:
#     print i[0],i[1]
# db.commit()
cur.execute('select person2.id,person1.name,person2.age from person1 right join person2 on person1.id=person2.id')
cur.execute('select max(id) As maxid from person1')
# cur.execute('alter table person1 add gender int(2)')
# cur.execute('alter table person1 modify gender char(20)')
cur.execute('alter table person1 drop gender')
rs=cur.fetchall()
# s=rs[0]
# print s[0],s[1],s[2]
# print rs[0]
# for i in rs:
#     print i[0],i[1],i[2]
db.commit()
db.close()