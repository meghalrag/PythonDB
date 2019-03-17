import pymysql
db=pymysql.connect('localhost','root','root')
cur=db.cursor()
cur.execute('use foriegndb')
db.commit()
class Student:
    def register(self,name,dept,ph,addr,user,passs):
        cur.execute('insert into register(name,dept,phno,address) values(%s,%s,%s,%s)',(name,dept,ph,addr))
        db.commit()
        id=cur.lastrowid
        self.loginInsert(user,passs,id)
    def loginInsert(self,user,passs,id):
        cur.execute('insert into login(username,password,fkid) values(%s,%s,%s)', (user,passs,id))
        db.commit()
    def logincheck(self,uname,passs):
        try:
            cur.execute('select * from login where username=%s and password=%s',(uname,passs))
            rs=cur.fetchone()
            if rs==None:
                print 'incorrect username or password'
            else:
                print rs[0],rs[1],rs[2],rs[3]
                print'login successfully'
        except(TypeError,pymysql.err.DataError),arg:
            print 'error occured----',arg

obj=Student()
while 1:
    print 'options\n1-register\n2-login\n3-exit'
    choi=input('enter your choice:')
    if choi==1:
        name=raw_input('enter your name:')
        dept=raw_input('enter dept:')
        ph=input('phno:')
        addr=raw_input('enter address:')
        user=raw_input('username:')
        passs=raw_input('password')
        obj.register(name,dept,ph,addr,user,passs)
    elif choi==2:
        uname=raw_input('enter username:')
        passs=raw_input('enter password:')
        obj.logincheck(uname,passs)
    elif choi==3:
        break
    else:
        print 'invalid'