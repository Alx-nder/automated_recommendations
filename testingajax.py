#!C:\Program Files\Python310\python.exe
# print("content-type: text/html;\n\n" )

######      THIS SCRIPT IS USED TO CREATE A LIST THAT REFLECTS PREFERENCES AS SEEN IN THE USER_PREF TABLE OF THE DATABASE. ONLY HERE, THE PREFERENCES ARE PAIRED TO THE INDICATOR THEY REPRESENT I.E: (A_LOCATION,INTERACTION_COUNT)


# all code contained in main function becuase this script will be imported

import sys
sys.path.append(r'C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages')
import pandas as pd
import mysql.connector

# connecting to database
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="virttour"
)

def main(username):

    location=[]
    #a variable to hold formatted/ tabbed prices in lists becuase we will get the interactions later
    price=[[0],[1000000],[2000000]]

    my_cursor= db.cursor()
    
    query="select house_location from listings"
    my_cursor.execute(query)
    updates=my_cursor.fetchall()   
    # remove duplicates 
    updates=set(updates)
    #back to list
    updates=list(updates)
    # populating lists from db records
    for row in range(0,len(updates)):
        location.append([[]])    
        location[row][0]=updates[row][0]

    # pandas method 
    query1="select * from user_pref"
    pref_data=pd.read_sql(query1,db)
    pref_data.set_index("username", inplace=True)
        
    for i in range(0,len(pref_data.columns)):
        if "price" not in pref_data.columns[i]:
            ##list[i].append dataframe[col][row]
            location[(i-3)][0]=pref_data.columns[i]
            location[(i-3)].append(pref_data.at[username, pref_data.columns[i]])
        else:
            price[i].append(pref_data.at[username, pref_data.columns[i]])   
            
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
	main("guest")

# print(main("guest"))