#!C:\Program Files\Python310\python.exe
print("content-type: text/html;\n\n" )


# all code contained in main

import sys
sys.path.append(r'C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages')
import cgi
import pandas as pd
import mysql.connector

def main():

    # connecting to database
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        database="virttour"
    )

    ## accept ajax body
    form=cgi.FieldStorage()
    username=form.getvalue("message_py")
    username="guest"
    print (username)
    location=[]
    #a variable to hold formatted/ tabbed prices in lists becuase we will get the interactions later
    price=[[0],[1000000],[2000000]]

    my_cursor= db.cursor()
    
    query="select location from listings"
    my_cursor.execute(query)
    updates=my_cursor.fetchall()
    # populating lists from db records
    for row in range(0,len(updates)):
        location.append([[]])    
        location[row][0]=updates[row][0]

    # pandas method 
    query1="select * from user_pref"
    pref_data=pd.read_sql(query1,db)
    pref_data.set_index("username", inplace=True)
        
    for i in range(0,len(pref_data.columns)):
        if "loc" in pref_data.columns[i]:
            ##list[i].append dataframe[col][row]
            location[(i-3)].append(pref_data[ pref_data.columns[i]][f"{username}"])
        else:
            price[i].append(pref_data[pref_data.columns[i]][f"{username}"])   
            
    #total interaction count
    location.append(0)
    # use len()-1 because last element is a int-interaction
    for i in range(0,len(location)-1):
        location[-1]+=location[i][-1]

    #total interaction count
    price.append(0)
    # use len()-1 because last element is a int-interaction
    for i in range(0,len(price)-1):
        price[-1]+=price[i][-1]

    return [location, price,-1]

# script to prevent the program from running when importing 
if __name__ == "__main__":
	main()	
print(main())