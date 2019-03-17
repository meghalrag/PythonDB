import pymysql
db=pymysql.connect('localhost','root','root')
con=db.cursor()
# cur.execute('create database login')
con.execute('use login')
# con.execute('create table login(username varchar(30),password varchar(20))')
while 1:

    print'options\n1-registration\n2-login\n3-exit\n4-showallusers\n5-delete user'
    choice = input('enter your choice:')
    if choice == 1:
        username = raw_input("enter username:")
        password = raw_input("enter password:")
        con.execute('insert into login values(%s,%s)', (username, password))
        print 'successful'
        con.execute('select * from login')
        rs=con.fetchall()
        for i in rs:
            print i[0], i[1]
        db.commit()
    elif choice == 2:
        user = raw_input("username:")
        passs = raw_input('password:')
        con.execute('select * from login')
        rs=con.fetchall()
        for i in rs:
            if i[0] == user and i[1] == passs:
                user = i[0]
                pas = i[1]
                while 1:
                    print 'options\n1-edit username\n2-password\n3-view prof\n4-logout'
                    log = input('your choice:')
                    if log == 1:
                        newuname = raw_input('new username:')
                        user = newuname
                        con.execute('update login set username=%s where username=%s and password=%s',
                                    (newuname, i[0], i[1]))
                        print'username updated'
                        db.commit()
                    elif log == 2:
                        newpass = raw_input('new password:')
                        pas = newpass
                        con.execute('update login set password=%s where username=%s and password=%s',
                                    (newpass, i[0], i[1]))
                        print'password updated'
                        db.commit()
                    elif log == 3:
                        con.execute('select * from login where username=%s and password=%s', (user, pas))
                        rs=con.fetchall()
                        for i in rs:
                            print 'username:', i[0]
                            print 'password:', i[1]
                    elif log == 4:
                        break
                break
    elif choice == 3:
        break
        db.close()
    elif choice == 4:
        s = raw_input('enter admin password:')
        if s == '12345':
            con.execute('select * from login')
            rs=con.fetchall()
            for i in rs:
                print i[0], i[1]
    elif choice == 5:
        s = raw_input('enter admin password:')
        if s == '12345':
            uname = raw_input('enter the username')
            upas = raw_input('enter password')
            con.execute('delete from login where username=%s and password=%s', (uname, upas))
            print 'successful'
            db.commit()
    else:
        print'invalid choice'