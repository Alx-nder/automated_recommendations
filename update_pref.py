#!C:\Program Files\Python310\python.exe
print("content-type: text/html;\n\n" )


import sys


sys.path.append(r'C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages')
import json
import cgi
import mysql.connector

# connecting to database
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="virttour"
)

## accept ajax body
form=cgi.FieldStorage()
username=json.loads(form.getvalue("message_py"))

# cursor = db.cursor()

# query=f"update user_pref set {} where username='guest'"
# cursor.execute(query)


# query=f"select * from user_pref where username='guest'"
# cursor.execute(query)

# records =json.dumps(cursor.fetchall()[0])

print(username["card_location"])