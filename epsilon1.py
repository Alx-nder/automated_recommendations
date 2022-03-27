#!C:\Program Files\Python310\python.exe
print("content-type: text/html;\n\n" )

import sys
from tkinter import N
sys.path.append(r'C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages')
import random
import json
import mysql.connector
import testingajax
import cgi
import pandas as pd


# connecting to database
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="virttour",
    autocommit=True
) 


## accept ajax body
form=cgi.FieldStorage()
username=form.getvalue("message_py")
grand_list=testingajax.main(username)

#function to randomly choose an item to display from nested lists
def randomiz(nth):
    if type(nth) is list:
        #prevent choosing last element - interaction count
        nth.pop(-1)
        return randomiz(random.choice(nth))       
    else:
        return nth

#this function takes a list and integer as parameters, checks to see what item in the list has the highest interaction count then returns/ prints that item.
def highofhigh(nested_list):
#base case -  if the list argument does not contain a nested list, return the first element of the current list and end.    
    if type(nested_list) is list:
        ### use the -1 as escape
        if nested_list[-1]==-1:
            nested_list.pop()
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
    else:
        return(nested_list)


def epsilon1(grand_list):  
#coin toss to choose recommendation form random or preferenced
  n1= random.uniform(0,1)
  n2= random.uniform(0,1)
  
  if n1 > n2:
      return randomiz(grand_list)   
  else:
      return highofhigh(grand_list)

rec_instance=epsilon1(grand_list) 

cursor = db.cursor()

# defining the Query to select records from the db where values returned from the algo and values in the db match
### use several parameters here than can chose from a consolidated price range
if type(rec_instance) is str:
    query = f"select * from listings where location ='{rec_instance}';"
else:
    query = f"select * from listings where price>{rec_instance} && price<{(rec_instance+1000000)} ;"

# getting records from the table
cursor.execute(query)

# storing all records from the 'cursor' object
records = cursor.fetchall()

# Showing the one of the possible returned listings
final_record=json.dumps(random.choice(records))
print(final_record)