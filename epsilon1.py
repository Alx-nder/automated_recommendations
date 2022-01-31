#!C:\Program Files\Python310\python.exe
print("content-type: text/html\n\n" )

import sys
sys.path.append(r'''C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages''')

#module to generate random numbers
import random

#module to manipulate sql database
import mysql.connector

#connecting to database
db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="virttour"
) 
mycursor= db.cursor()
 
#prices min, max, interaction count
p1=[10,10,2]
p2=[10,6,1]
p3=[10,2,3]

#addresses codes, interaction count
a1=['va',2]
a2=['md',1]
a3=['ja',3]

#list of prices and an interaction count
price=[p1,p2,p3,0]

#list of addresses and an interaction count
address=[a1,a2,a3,1]
grand_list=[price,address]

#this function takes a list and integer as parameters, checks to see what item in the list has the highest interaction count then returns/ prints that item.
def highofhigh(nested_list,action):
#base case -  if the list argument does not contain a nested list, return the first element of the current list and end.    
    if type(nested_list[0]) != type([list]) and type(nested_list[-1]== type(int)):
        print(nested_list[0])
        return nested_list[0]
    
    interaction_count=nested_list[0][-1]
    max_index=0
    
#traverses list to find the highest nested interaction count
    for x in range(0, len(nested_list)):
        if type(nested_list[x]) != list and type(nested_list[-1]== int):
            break
        elif nested_list[x][-1] > interaction_count:
            interaction_count=nested_list[x][-1]
            max_index=x
    #running action to update interaction count
    nested_list[max_index][-1]+=action
    
    secondnestedlist=nested_list[max_index]
    highofhigh(secondnestedlist, action)

#function to randomly choose an item to display from nested lists
def randomiz(nth,action):
    #prevent choosing last element - interaction count
    if type(nth[0]) != list and type(nth[-1]== int):
        print(nth[0])
        return nth[0]
    
    #check if the list argument is the grand_list, which has no interaction count variable   
    elif type(nth[-1])!= int:
        first=random.choice(nth)
        #first is a list
        first[-1]+=action
        randomiz(first,action)
    #recursive
    else:    
        first = random.randrange(0,len(nth)-1)
        nth[first][-1]+=action
        randomiz(nth[first],action)

def epsilon1(grand_list,action):  
#coin toss to choose recommendation form random or preferenced
  n1= random.uniform(0,1)
  n2= random.uniform(0,1)
  
  if n1 > n2:
      randomiz(grand_list,action)
  else:
      highofhigh(grand_list,action)
      
epsilon1(grand_list,1)