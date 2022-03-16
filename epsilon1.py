#!C:\Program Files\Python310\python.exe
print("content-type: text/html;\n\n" )

import sys
from tkinter import N
sys.path.append(r'C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages')
import random
import json
import mysql.connector
import testingajax
# import cgi
# import pandas as pd

## recieveing the username as a vvariable from the ajax call
# form=cgi.FieldStorage()
# current_user=form.getvalue("message_py")

# connecting to database
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="virttour"
) 

#prices min, max, interaction count
p1=[3524432,2]
p2=[25140234,1]
p3=[1052442,3]
p4=[3125476,3]
p5=[1000000,3]

#addresses codes, interaction count
a1=[1125476,2]
a2=[25140234,1]
a3=[1052442,3]
a4=[3524432,3]
a5=[1000000,2]

#list of prices and an interaction count
price=[p1,p2,p3,p4,p5,0]

#list of addresses and an interaction count
location=[a1,a2,a3,a4,a5,1]
# grand_list=[price,location]
grand_list=testingajax.main()

#this function takes a list and integer as parameters, checks to see what item in the list has the highest interaction count then returns/ prints that item.
def highofhigh(nested_list):
#base case -  if the list argument does not contain a nested list, return the first element of the current list and end.    
    if type(nested_list[0]) != type([list]) and type(nested_list[-1]== type(int)):
        return nested_list[0]

    #we assume the first element has the highest interaction count 
    interaction_count=nested_list[0][-1]
    #the position of the list with the higher/highest interaction count
    max_index=0
    
#traverses list to find the highest nested interaction count
    for x in range(0, len(nested_list)):
        # end of nested
        if type(nested_list[x]) != list and type(nested_list[-1]== int):
            break
        elif nested_list[x][-1] > interaction_count:
            interaction_count=nested_list[x][-1]
            max_index=x
            
    secondnestedlist=nested_list[max_index] #declaring the list with highest interaction count
    return highofhigh(secondnestedlist)

#function to randomly choose an item to display from nested lists
def randomiz(nth):
    if type(nth) is list:
        #prevent choosing last element - interaction count
        if (type(nth[0]) != list or type(nth[0]) == str) and type(nth[-1]) is int:
            print(nth[0],'cow')
            return nth[0]
        else:
            randomiz(random.choice(nth.pop()))       
        
    else:
        return(nth)

def epsilon1(grand_list):  
#coin toss to choose recommendation form random or preferenced
  n1= random.uniform(0,1)
  n2= random.uniform(0,1)
  
  if n1 > n2:
      return randomiz(grand_list)   
  else:
      return highofhigh(grand_list)

rec_instance=epsilon1(grand_list) 

print(rec_instance,"tretrdgrdrg")

cursor = db.cursor()

# defining the Query to select records from the db where values returned from the algo and values in the db match
### use several parameters here than can chose from a consolidated price range
if type(rec_instance) is str:
    query = f"select * from listings where location ='{rec_instance}';"
else:
    query = f"select * from listings where price>{rec_instance} and price<{rec_instance+100000};"

# getting records from the table
cursor.execute(query)

# storing all records from the 'cursor' object
records = cursor.fetchall()

# Showing the one of the possible returned listings
final_record=json.dumps(random.choice(records))
print(final_record)