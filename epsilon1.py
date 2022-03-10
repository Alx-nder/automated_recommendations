#!C:\Program Files\Python310\python.exe
print("content-type: text/html;\n\n" )

import sys
sys.path.append(r'C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages')

import random
import json
import mysql.connector


# connecting to database
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
a1=[1125476,2]
a2=[25140234,1]
a3=[1052442,3]

#list of prices and an interaction count
price=[p1,p2,p3,0]

#list of addresses and an interaction count
location=[a1,a2,a3,1]

# xd=[]
# variable_name = [k for k, v in locals().items() if v==xd][0] 
# print("Your variable name is " + variable_name)

# location=[]
# price=[]
grand_list=[price,location]

# my_cursor= db.cursor()

# def db_to_list(list_from_table, list_name):
#     query=f"select {list_name} from listings"
#     my_cursor.execute(query)
#     updates=my_cursor.fetchall()

#     # populating lists from db records
#     for row in range(0,len(updates)):
#         list_from_table.append([[]])    
#         list_from_table[row][0]=updates[row][0]

# db_to_list(location,"location")
# db_to_list(price,"price")

# query="select * from user_pref"
# my_cursor.execute(query)
# preferences=my_cursor.fetchall()
# print(preferences)
# # to upload interaction data
# for row in range(0,len(preferences)):
#     interactions=0
#     for x in preferences[row]:
#         x=+1
#         price[x].append(preferences[row][x])
    
    

# print(price)
# print(location)

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

cursor = db.cursor()

# defining the Query to select records from the db where values returned from the algo and values in the db match
query = f"select * from listings where price = {rec_instance} or location={rec_instance};"

# getting records from the table
cursor.execute(query)

# storing all records from the 'cursor' object
records = cursor.fetchall()

# Showing the one of the possible returned listings
# final_record=json.dumps(random.choice(records))
js_final_record="var rec_dict=".__add__(json.dumps(random.choice(records)))
final_record=json.dumps(random.choice(records))
print(final_record)