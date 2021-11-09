import mysql.connector
mydb = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', password='RajkumarAsktoecho#@543210', database='busmanagment')
mycursor = mydb.cursor()

# mycursor.execute('create table station(scode varchar(15) not null, sname varchar(100), slocation varchar(100), primary key (scode))')
# mycursor.execute('create table route(rid int not null check(rid>0), start_scode varchar(10) not null, dest_scode varchar(10) not null, distance int, depart_time time, name varchar(30), primary key (rid), foreign key (start_scode) references station(scode) on delete cascade, foreign key (dest_scode) references station(scode) on delete cascade)')
# mycursor.execute('create table bus(bid int, name varchar(50), numplate varchar(8), type varchar(20), model varchar(20), seats int, rid int, scode varchar(10) , primary key (bid), foreign key (scode) references station(scode) on delete set null, foreign key (rid) references route(rid) on delete set null )')
# mycursor.execute('create table employee(eid int, name varchar(50), designation varchar(20), bid int, scode varchar(10), salary int, primary key (eid), foreign key (bid) references bus(bid) on delete set null, foreign key (scode) references station(scode) on delete set null)')
# mycursor.execute('create table bushaults(rid int, start varchar(10) not null, end varchar(10) not null, primary key (rid))')
# mycursor.execute('create table ticket(tid int, bid int, rid int, fare float, pass_name varchar(50),	 pass_mobno varchar(10), age int, gender varchar(1), start varchar(10), end varchar(10), timestamp time, primary key (tid), foreign key (bid) references bus (bid) on delete set null, foreign key (rid) references route(rid) on delete set null)')
# mycursor.execute('create table passenger(tid int, pass_name varchar(50), pass_mobno varchar(10), age int, gender varchar(1), rid int, start varchar(10), end varchar(10), timestamp time, primary key(tid), foreign key (tid) references ticket(tid))')
# mycursor.execute('show tables')
# for x in mycursor:
#     print(x)

# f = open("station")
# for x in range(0, 15):
#   y = f.readline()
#   z = f.readline()
#   u = f.readline()
#   sql = "INSERT INTO station (scode, sname, slocation) VALUES (%s, %s, %s)"
#   val = (y.rstrip("\n"), z.rstrip('\n'), u.rstrip('\n'), )
#   mycursor.execute(sql, val)
#   mydb.commit()
# f.close()

# f = open('route')
# x = int(f.readline())
# y = f.readline()
# z = f.readline()
# a = int(f.readline())
# b = f.readline()
# c = f.readline()
# sql = "INSERT INTO route (rid, start_scode, dest_scode, distance, depart_time, name) VALUES (%s, %s, %s, %s, %s, %s, )"
# val = (x, y.rstrip('\n'), z.rstrip('\n'), a, b.rstrip('\n'), c.rstrip('\n'), )
# mycursor.execute(sql, val)
# mydb.commit()
# f.close()
#
# mycursor.execute('select * from route')
# for x in mycursor:
#     print(x)
