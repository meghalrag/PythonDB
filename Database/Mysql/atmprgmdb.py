import pymysql
db=pymysql.connect('localhost','root','root')
cur=db.cursor()
cur.execute('use bankdatabase')
class ATM:
    def insert(self,id,name,address,phno,accno,atmno,balance):
        self.id=id
        self.name=name
        self.address=address
        self.phno=phno
        self.accno=accno
        self.atm=atmno
        self.balance=balance
    def addcustomer(self):
        try:
            cur.execute('insert into bankdatas(id,customer_name,phonenumber,address,account_no,atm_no,acc_balance) values(%s,%s,%s,%s,%s,%s,%s)'
                        '',(self.id,self.name,self.phno,self.address,self.accno,self.atm,self.balance))
            print''
            print"\033[1;34;42m",
            print 'account added successfully'
            print"\033[1;34;48m",
        except (TypeError,pymysql.err.DataError),arg:
            print "\033[0;30;41m",
            print '!!!!!account not set because',arg
            print"\033[1;34;48m",
            print 'please try again'
        finally:
            db.commit()
    def checkbalance(self,acc,atmno):
        try:
            cur.execute('select acc_balance from bankdatas where account_no=%s and atm_no=%s', (acc, atmno))
            rs = cur.fetchone()
            rs[0]
            print "\033[1;31;47m",
            print 'your balance is INR', rs[0]
            print"\033[1;34;48m",
        except TypeError,arg:
            print "\033[0;30;41m",
            print '!!!!check your accno and atmno--------', arg
            print"\033[1;34;48m",
    def deposit(self,acc,atm,deposit):
        try:
            cur.execute('select acc_balance from bankdatas where account_no=%s and atm_no=%s', (acc, atm))
            rs = cur.fetchone()
            rs[0]
            total=rs[0]+int(deposit)
            cur.execute('update bankdatas set acc_balance=%s where account_no=%s',(total,acc))
            db.commit()
            print'cash deposited successfully'
            print "\033[1;31;47m",
            print 'balance is INR',total
            print"\033[1;34;48m",
        except TypeError,arg:
            print "\033[0;30;41m",
            print '!!!!check your accno and atmno--------', arg
            print"\033[1;34;48m",
    def withdraw(self,acc,atm,withdr):
        try:
            cur.execute('select acc_balance from bankdatas where account_no=%s and atm_no=%s',(acc,atm))
            rs=cur.fetchone()
            rs[0]
            total=rs[0]-int(withdr)
            if total<0:
                print "\033[0;30;41m",
                print'please enter an amount in range INR',rs[0]
                print"\033[1;34;48m",
            else:
                cur.execute('update bankdatas set acc_balance=%s where account_no=%s', (total, acc))
                db.commit()
                print'cash withdrawed'
                print "\033[1;31;47m",
                print 'Remaining balance is INR', total
                print"\033[1;34;48m",
        except TypeError,arg:
            print "\033[0;30;41m",
            print '!!!!check your accno and atmno--------',arg
            print"\033[1;34;48m",
    def display(self,acc,atm):
        try:
            cur.execute('select * from bankdatas where account_no=%s and atm_no=%s',(acc,atm))
            rs=cur.fetchone()
            print "\033[1;30;47m",
            rs[1]
            print 'name:',rs[1]
            print 'phone no:',int(rs[2])
            print 'address:',rs[3]
            print 'accno:',rs[4]
            print 'account balance:',rs[6]
            print"\033[1;34;48m",
        except TypeError,arg:
            print "\033[0;30;41m",
            print '!!!!check your accno and atmno--------',arg
            print"\033[1;34;48m",
    def fundTransfer(self,amt,accf,acct,accnt):
        cur.execute('select * from bankdatas where account_no=%s',(accf))
        rs=cur.fetchone()
        atmno=input('enter your atm no:')
        if rs[5]==atmno:
            tamt=rs[6]-amt
            if tamt<0:
                print 'insufficient balance'
            else:
                cur.execute('update bankdatas set acc_balance=%s where account_no=%s',(tamt,accf))
                cur.execute('update bankdatas set acc_balance=%s where account_no=%s',(amt,acct))
                db.commit()
                print 'amount tansfered'
bal=0
obj=ATM()
cur.execute('select max(id),max(account_no) from bankdatas')
rs=cur.fetchone()
accno=rs[1]
id=rs[0]
if accno==None:
    accno=10000
    id=0
while 1:
    # cur.execute('delete from bankdatas where id=2')
    # db.commit()
    print"\033[1;34;48m",
    print '\noptions\n1-addacc\n2-deposite\n3-checkbalance\n4-withdraw\n5-display\n6-Fund transfer\n7-exit'
    choice=input('your choice:')
    if choice==1:
        # print accno,
        # print id
        accno = accno + 1
        id = id + 1
        flag = 'ph'
        name=raw_input("your name:")
        addr=raw_input("address:")
        while 1:
            if flag=='ph':
                phno = raw_input('phno:')
                if len(phno)!=10:
                    print "\033[0;30;41m",
                    print 'phone no must be 10 num'
                    print"\033[1;34;48m",
                    flag='ph'
                    continue
            atm=raw_input('choose your atmno:')
            if len(atm)!=4:
                print "\033[0;30;41m",
                print'atm no must be 4 numbers'
                print"\033[1;34;48m",
                flag='atm'
                continue
            break
        print 'details'
        print 'name:',name
        print 'address:',addr
        print 'phoneno:',phno
        print 'atmno:',atm
        print "\033[1;30;47m",
        y=raw_input('can i proceed(y/n):')
        print"\033[1;34;48m",
        if y=='y':
            obj.insert(id,name,addr,phno,accno,atm,bal)
            obj.addcustomer()
        else:
            exit()
    if choice==2:
        depo=raw_input('enter amount:')
        cho = raw_input('enter your account num:')
        atmn = raw_input('enter your atm num:')
        obj.deposit(cho,atmn,depo)
    if choice==3:
        cho = raw_input('enter your account num:')
        atmn = raw_input('enter your atm num:')
        obj.checkbalance(cho,atmn)
    if choice==4:
        withdr = raw_input('enter amount:')
        cho = raw_input('enter your account num:')
        atmn = raw_input('enter your atm num:')
        obj.withdraw(cho,atmn,withdr)
    if choice==5:
                cho=raw_input('enter your account num:')
                atmn=raw_input('enter your atm num:')
                obj.display(cho,atmn)
    if choice==6:
        accnof=raw_input('enter your account num:')
        accnot=raw_input('enter the account num totransfer:')
        accnamet=raw_input('enter the name of acc holder:')
        amount=input('entet the amount to transfer:')
        obj.fundTransfer(amount,accnof,accnot,accnamet)
    if choice==7:
        print "\033[1;31;47m",
        print " ***thanks*****"
        db.close()
        break