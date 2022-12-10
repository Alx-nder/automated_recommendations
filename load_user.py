#!C:\Users\Tyreek ALEXANDER\AppData\Local\Programs\Python\Python310\python.exe
# print("content-type: text/html;\n\n" )

######      THIS SCRIPT IS USED TO CREATE lists THAT REFLECTS PREFERENCES AS SEEN IN THE USER_PREF TABLE OF THE DATABASE. 
# 
# HERE, THE tags (say specific locations or price tabs) ARE PAIRED TO THE number of times a particular user clicks on it 
# For example location_5=[a_location, interaction_count] LOOKS LIKE location_5=["Maryland",10]. 
# This is done for all tags. 
# 
# Next, where applicable, the common tags are nested into a bigger list and the tally of the interactions appended to the end. 
# 
# For example global_tag[example_tag_1, example_tag_1,...example_tag_1, collective_interaction_count] LOOKS LIKE locations[["maryland",4],["Virginia",2],...["hawaii",0], 69]
#
# global tags are then nested into a final list for the recommendation algorithm to traverse and use
#For example final_list=[locations, prices ... any_other_global_tags, -1]
# the -1 is used as an escape character

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
    #a variable to hold formatted/ consolidated prices in lists because we will get the interactions later
    price=[[0],[1000000],[2000000]]

    my_cursor= db.cursor()    

    # get the locations
    query="select house_location from listings"
    my_cursor.execute(query)
    results=my_cursor.fetchall()   
    # remove location duplicates 
    results=set(results)
    #back to list
    results=list(results)
    # populating location lists from db records (results) with the actual location names
    for row in range(0,len(results)):
        location.append([[]])    
        location[row][0]=results[row][0]

    # pandas to load the preference data table as a dataframe
    query1="select * from user_pref"
    pref_data=pd.read_sql(query1,db)
    pref_data.set_index("username", inplace=True)
        
    #reading the interaction data then adding it to the list
    for i in range(0,len(pref_data.columns)):
        if "price" not in pref_data.columns[i]:
            ##list[i].append dataframe[col][row]
            location[(i-3)][0]=pref_data.columns[i]
            location[(i-3)].append(pref_data.at[username, pref_data.columns[i]])
        else:
            price[i].append(pref_data.at[username, pref_data.columns[i]])   
            
    #total interaction count - we need a tally of all interactions with locations 
    location.append(0)
    # use len()-1 because last element is an int-interaction
    for i in range(0,len(location)-1):
        location[-1]+=location[i][-1]

    
    # tallies
    #total interaction count - we need a tally of all interactions with prices
    price.append(0)
    # use len()-1 because last element is a int-interaction
    for i in range(0,len(price)-1):
        price[-1]+=price[i][-1]

    return [location, price,-1]

# script to prevent the program from running when importing 
if __name__ == "__main__":
	main("guest")

## keeping a tally of all the interactions based on the tags - location and price is used later to see if one is more dominant than the other. 
## and although a click will reward both tags, search functions may be used to determine which tag is superior.