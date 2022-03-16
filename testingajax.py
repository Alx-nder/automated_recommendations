#!C:\Program Files\Python310\python.exe
print("content-type: text/html;\n\n" )



import sys
sys.path.append(r'C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages')
import cgi
import pandas as pd
import mysql.connector

# all code contained in main
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

    location=[]

    #a variable to hold formatted/ tabbed prices in lists becuase we will get the interactions later
    price=[[0],[1000000],[2000000]]
    # grand_list=[price,location]

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


    # pandas method 
    query1="select * from user_pref"
    pref_data=pd.read_sql(query1,db)
    pref_data.set_index("username", inplace=True)
        
    for i in range(0,len(pref_data.columns)):
        if "loc" in pref_data.columns[i]:
            location[i-3].append(pref_data[pref_data.columns[i]]["t@y.com"])
        else:
            price[i].append(pref_data[pref_data.columns[i]]["t@y.com"])   
            
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

    return [location, price]

# script to prevent the program from running when importing 
if __name__ == "__main__":
	main()	
