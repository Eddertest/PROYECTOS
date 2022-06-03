import bcrypt
import argparse
import sys
import mysql.connector
from datetime import datetime


#MAIN PROGRAM ###########
parser = argparse.ArgumentParser()
parser.add_argument('csvfile', help='CSV file name containing users data: username, full name, email, clear password')
args= parser.parse_args()


#READ CURRENT DATE#################
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#CONECT TO DATABASE############

try:
    conn = mysql.connector.connect (user='usuario', password = 'AQUI VA LA CLAVE', host '127.0.0.1', database='db')
    cursor = conn.cursor()
except Exception as e:
    print(e)
    quit()


#READ CSV FILE ##############
lines =[(line.rstrip('\n')) for line in open(args.csvfile)]

for line in lines:
    username = line.split(',')[0]
    name = line.split(',')[1]
    email = line.split(',')[2]
    password = line.split(',')[3]

    

#ENCRYPT THE PASSWORD ##############
b = password.encode("utf-8")
hashed = bcrypt.hashpw(b, bcrypt.gensalt(rounds=10))
aux = str(hashed)
aux2 = aux[2:]
password = aux2[:-1]



#GET CURRENT TIMESTAMP##############
time = datetime.now()
current_time = time.strftime("%Y-%m-%d %H:%M:%S")
print(username, name, email, password)



print("BEGIN")
##INSERT USER IN OSTICKET DATABASE ##############
try:
    sql = "START TRANSACTION;"
    cursor.execute(sql)

    print("inserting ost_user")
    sql ="INSERT INTO ost_user(org_id, default_email_id, name, created, updated) VALUES (%s,%s,%s,%s,%s)"

    cursor.execute(sql,(0,0,name,current_time,current_time))


#ENCRYPT THE PASSWORD ##############
sql = "SELECT MAX(id) FROM ost_user;"
cursor.execute(sql)
rows = cursor.fetchall()
ID = int(rows[0][0])

print("inserting ost_user_email")
sql ="INSERT INTO ost_user_email (user_id, address) VALUES (%s,%s)"cursor.excecute(sql,(ID, email))


print("inserting ost_user_cdata")
sql ="INSERT INTO ost_user_cdata (user_id, username) VALUES (%s,%s)"
cursor.excecute(sql,(ID, username))



print("inserting ost_user_account")
sql ="INSERT INTO ost_user_account (user_id, status,timezone,username,passwd,extra) VALUES (%s,%s,%s,%s,%s,%s)"
cursor.excecute(sql,(ID, 1,"America/Bogota",username, password, '{"browser_lang":"es MX"}'))


print("inserting ost_form_entry")
sql ="INSERT INTO form_entry (form_id, object_id,object_type,sort,created,updated) VALUES (%s,%s,%s,%s,%s,%s)"
cursor.excecute(sql,(1, ID,"U",1, current_time, current_time))



"""
print("select ost_user_email")
sql = "SELECT id from ost_user_email WHERE address='%s'"
cursor.excecute(sql,(email))
rows = cursor.fetchall()
print(rows)
emailID = int(rows[0][0])


print ("updating ost_user"")
sql = "UPDATED ost_user SET default_email_id=%s WHERE id=%s"
cursor.excecute(sql,(emailID,ID))

"""


sql="COMMIT;"
cursor.excecute(sql)


except Exception as e:
print (e)
quit()

#conn.commit()


conn.close()















