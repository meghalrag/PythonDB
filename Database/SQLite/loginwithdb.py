import sqlite3
con=sqlite3.connect('userdb')
# con.execute('create table login(username char(50),password char(20));')
while 1:
    print'options\n1-registration\n2-login\n3-exit\n4-showallusers\n5-delete user'
    choice=input('enter your choice:')
    if choice==1:
        username=raw_input("enter username:")
        password=raw_input("enter password:")
        con.execute('insert into login values(?,?)',(username,password))
        print 'successful'
        rs=con.execute('select * from login')
        for i in rs:
            print i[0],i[1]
        con.commit()
    elif choice==2:
        user=raw_input("username:")
        passs=raw_input('password:')
        rs = con.execute('select * from login')
        for i in rs:
            if i[0]==user and i[1]==passs:
                user=i[0]
                pas=i[1]
                while 1:
                    print 'options\n1-edit username\n2-password\n3-view prof\n4-logout'
                    log=input('your choice:')
                    if log==1:
                        newuname=raw_input('new username:')
                        user=newuname
                        con.execute('update login set username=? where username=? and password=?',(newuname,i[0],i[1]))
                        print'username updated'
                        con.commit()
                    elif log==2:
                        newpass = raw_input('new password:')
                        pas=newpass
                        con.execute('update login set password=? where username=? and password=?',
                                    (newpass, i[0], i[1]))
                        print'password updated'
                        con.commit()
                    elif log==3:
                        rs=con.execute('select * from login where username=? and password=?',(user,pas))
                        for i in rs:
                            print 'username:',i[0]
                            print 'password:',i[1]
                    elif log==4:
                        break
                break
    elif choice==3:
        break
    elif choice==4:
        s=raw_input('enter admin password:')
        if s=='12345':
            rs=con.execute('select * from login')
            for i in rs:
                print i[0],i[1]
    elif choice==5:
        s = raw_input('enter admin password:')
        if s == '12345':
            uname=raw_input('enter the username')
            upas=raw_input('enter password')
            con.execute('delete from login where username=? and password=?',(uname,upas))
            con.commit()
            # for i in rs:
            #     print i[0], i[1]