#!C:\Program Files\Python310\python.exe
print("content-type: text/html;\n\n" )


import sys


sys.path.append(r'C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages')
import json
import cgi
import mysql.connector
import pandas as pd

# connecting to database
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="virttour"
)

# ## accept ajax body
form=cgi.FieldStorage()

# loads json the obj sent from js 
js_postdata=json.loads(form.getvalue("message_py"))
location_pref=js_postdata["card_location"]
current_user=js_postdata["username"]


query1="select * from user_pref"
pref_data=pd.read_sql(query1,db)
pref_data.set_index("username", inplace=True)

### a single record located at [col][row]
interaction=pref_data[location_pref][current_user]

### updating the interaction

cursor = db.cursor()
##using backquotes in the event of non-conformant field names
query=f"update user_pref set `{location_pref}`={interaction+1} where username='{current_user}'"
cursor.execute(query)


tquery=f"select * from user_pref where username='guest'"
cursor.execute(tquery)

records =json.dumps(cursor.fetchall())

print(records)