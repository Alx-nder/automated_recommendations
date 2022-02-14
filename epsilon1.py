#!C:\Program Files\Python310\python.exe
print("content-type: text/html\n\n" )

import sys
from traceback import print_exception
sys.path.append(r'''C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages''')

#module to generate random numbers
import random
import json

#module to manipulate sql database
import mysql.connector

#connecting to database
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="virttour"
) 
#prices min, max, interaction count
p1=[1125476,10,2]
p2=[25140234,6,1]
p3=[1052442,2,3]


#addresses codes, interaction count
a1=[1,2]
a2=[30,1]
a3=[45,3]

#list of prices and an interaction count
price=[p1,p2,p3,0]
# price=[]
#list of addresses and an interaction count
address=[a1,a2,a3,1]
# address=[]
grand_list=[price,address]

# mycursor= db.cursor()

# query="select location from listings"
# mycursor.execute(query)
# prec=mycursor.fetchall()

# populating lists from db records
# for row in range(0,len(prec)):
#     address.append([[]])    
#     address[row][0]=prec[row][0]

# # interaction count
# address.append(4)

# query="select price from listings"

# mycursor.execute(query)
# prec=mycursor.fetchall()

# populating list from db records
# for row in range(0,len(prec)):
#     price.append([[]])    
#     price[row][0]=prec[row][0]

# print(price)
# print(address)

#this function takes a list and integer as parameters, checks to see what item in the list has the highest interaction count then returns/ prints that item.
def highofhigh(nested_list,action):
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
            
    #running action to update interaction count
    nested_list[max_index][-1]+=action
    secondnestedlist=nested_list[max_index] #declaring the list with highest interaction count
    
    return highofhigh(secondnestedlist, action)

#function to randomly choose an item to display from nested lists
def randomiz(nth,action):
    #prevent choosing last element - interaction count
    if type(nth[0]) != list and type(nth[-1]== int):
        return nth[0]
        
    #check if the list argument is the grand_list, which has no interaction count variable   
    elif type(nth[-1])!= int:
        first=random.choice(nth)
        #first is a list
        first[-1]+=action
        return randomiz(first,action)
    #recursive
    else:    
        first = random.randrange(0,len(nth)-1)
        nth[first][-1]+=action
        return randomiz(nth[first],action)

def epsilon1(grand_list,action):  
#coin toss to choose recommendation form random or preferenced
  n1= random.uniform(0,1)
  n2= random.uniform(0,1)
  
  if n1 > n2:
      return randomiz(grand_list,action)   
  else:
      return highofhigh(grand_list,action)
      
rec_instance=epsilon1(grand_list,1) 
print(rec_instance)

# cursor = db.cursor()

## defining the Query
# query = "select * from listings where add = %s;"

## getting records from the table
# cursor.execute(query, (rec_instance, ))

## fetching all records from the 'cursor' object
# records = cursor.fetchall()

# r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]

## Showing the data
# print(f"json: {json.dumps(records)}")
# print(records)

# for record in records:
#     print(json.dumps(record))
#     print (f"json: {json.dumps(record)}")