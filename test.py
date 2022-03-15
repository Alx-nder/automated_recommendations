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


location=[]
price=[]
grand_list=[price,location]

my_cursor= db.cursor()
# function that creates a list from the data in a specified table column 
def db_to_list(list_from_table, list_name):
    # selecting and reading
    query=f"select {list_name} from listings"
    my_cursor.execute(query)
    updates=my_cursor.fetchall()

    # populating lists from db records
    for row in range(0,len(updates)):
        list_from_table.append([[]])    
        list_from_table[row][0]=updates[row][0]

db_to_list(location,"location")
db_to_list(price,"price")

print(location,"\n\n",price)


query1="select * from user_pref"

# pandas method 
pref_data=pd.read_sql(query1,db)
pref_data.set_index("username", inplace=True)
print(pref_data)

       
for i in range(0,len(pref_data.columns)):
    if "loc" in pref_data.columns[i]:
        
        location[i-3].append(pref_data[pref_data.columns[i]]['t@y.com'])
    else:
        price[i].append(pref_data[pref_data.columns[i]]['t@y.com'])    

print(location,"\n\n",price)