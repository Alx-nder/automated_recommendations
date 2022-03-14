#!C:\Program Files\Python310\python.exe
print("content-type: text/html;\n\n" )
import cgi
import pandas as pd
import mysql.connector

# connecting to database
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="virttour"
)

# form=cgi.FieldStorage()
# user_speech=form.getvalue("message_py")

# print(user_speech,"adawawd")


query1="select * from user_pref"

# pandas method 
pref_data=pd.read_sql(query1,db)
pref_data.set_index("username", inplace=True)
# print(pref_data)

if "price" in pref_data.columns:
    print("true")
else:
    print("false")
