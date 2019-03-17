import pymysql
db=pymysql.connect('localhost','root','root')
cur=db.cursor()
# cur.execute('create database student')
# cur.execute('drop database student3')
# cur.execute('create table student ')
# cur.execute('select * from sampletable')
# rs=cur.fetchall()
# for i in rs:
#     print i[0],i[1]
