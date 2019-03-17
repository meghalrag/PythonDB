import pymysql
db=pymysql.connect('localhost','root','root')
cur=db.cursor()
cur.execute('use bankforiegndb')
class ATM:
    def addacc(self,name,addr,phno,atmno,user,passs,bal,accno):
        cur.execute('insert into register(name,address,phno,atmno) values(%s,%s,%s,%s)', (name, addr, phno, atmno))
        db.commit()
        id=cur.lastrowid
        self.login(accno,user,passs,id,bal)
    def login(self,accno,user,passs,id,bal):
        cur.execute('insert into login(accno,username,password,fkid) values(%s,%s,%s,%s)', (accno,user,passs,id))
        db.commit()
        id = cur.lastrowid
        self.balance(bal,id)
    def balance(self,bal,id):
        cur.execute('insert into balance(balance,fkid) values(%s,%s)', (bal,id))
        db.commit()
        print'acount added successfully'
    def deposit(self,acc):
        cur.execute('select * from login join balance on login.id=balance.fkid and login.accno=%s', acc)
        rs = cur.fetchone()
        print rs
        amt = input('enter the amount:')
        total = rs[6] + amt
        print total
        print rs[5]
        cur.execute('update balance set balance=%s where id=%s', (total, rs[5]))
        db.commit()
        print 'update successfully'
    def checkbalance(self,accno):
        cur.execute('select * from login join balance on login.id=balance.fkid '
                                        'join register on login.fkid=register.id '
                                        'and login.accno=%s',accno)
        rs=cur.fetchone()
        print rs
        atm=raw_input('enter password:')
        if rs[3]==atm:
            print 'balance is:INR',rs[6]
    def withdraw(self):
        pass
    def display(self,accno,passwd):
        cur.execute('select * from login')
        rs=cur.fetchall()
        usern=accno
        try:
            accno=int(accno)
        except ValueError,arg:
            print''
        for i in rs:
            if i[1]==accno and i[3]==passwd or i[2]==usern and i[3]==passwd:
                cur.execute('select * from register where id=%s',(i[4]))
                rs=cur.fetchone()
                cur.execute('select * from balance where fkid=%s',(i[4]))
                rc=cur.fetchone()
                print"\033[1;31;48m",
                print 'name:',rs[1]
                print 'username:',i[2]
                print 'password:',i[3]
                print 'address:',rs[2]
                print 'phone no:',int(rs[3])
                print 'account num:',i[1]
                print 'atmno:',rs[4]
                print 'balance:',rc[1]
                print"\033[1;34;48m"
                break
ob=ATM()
cur.execute('select max(accno) from login')
rs=cur.fetchone()
if rs[0]==None:
    accno=1000
else:
    accno=rs[0]
print accno

while 1:
    print'option\n1-addacc\n2-deposit\n3-checkbalance\n4-withdraw\n5-display\n6-exit'
    choice=input('enter your choice:')
    if choice==1:
        accno=int(accno)+1
        name=raw_input('enter your name:')
        addr=raw_input('enter address:')
        phno=input('enter phone no:')
        username=raw_input('enter username')
        password=raw_input('enter a password')
        minbalance=input('set a min balance:')
        atmno=input('choose atm no:')
        ob.addacc(name,addr,phno,atmno,username,password,minbalance,accno)
    elif choice==2:
        acc=input('enter the account number:')
        ob.deposit(acc)
    elif choice==3:
        acc=input('enter the accno:')
        ob.checkbalance(acc)
    elif choice==4:
        ob.withdraw()
    elif choice==5:
        accno=raw_input('enter accno: or username:')
        password=raw_input('enter your password:')
        ob.display(accno,password)
    elif choice==6:
        break
