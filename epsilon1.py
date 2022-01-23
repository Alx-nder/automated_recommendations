#!C:\Program Files\Python310\python.exe
print("content-type: text/html\n\n" )


import sys
sys.path.append(r'''C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages''')

import random

from numpy import true_divide

def highofhigh(firstnestedlist,action):
    
    if type(firstnestedlist[0]) != type([list]) and type(firstnestedlist[-1]== type(int)):
    
        print(firstnestedlist)
        return firstnestedlist
    
    max=firstnestedlist[0][-1]
    maxi=0

    for x in range(0, len(firstnestedlist)):
        #is this necessary? it checks if nested
        if type(firstnestedlist[x]) != list and type(firstnestedlist[-1]== int):
            break

        elif firstnestedlist[x][-1] > max:
            max=firstnestedlist[x][-1]
            maxi=x
    #running action to change values
    firstnestedlist[maxi][-1]+=action
    
    #or say if index0= list run func
    #newlist=mass[maxi]
    #if type(newlist[x]) != "list":
    #    return newlist
    #print(firstnestedlist)
    secondnestedlist=firstnestedlist[maxi]
    highofhigh(secondnestedlist, action)

 
#prices min, max, count
p1=[7,10,2]
p2=[3,6,1]
p3=[1,2,3]

a1=['va',2]
a2=['md',1]
a3=['ja',3]

price=[p1,p2,p3,0]
address=[a1,a2,a3,1]
mass=[price,address]

def randomiz(nth,action):
    #prevent choosing last
    if type(nth[0]) != list and type(nth[-1]== int):
      
        print(nth)
        return nth
    #check if first    
    ###something weird happened here 
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

      
def epsilon1(mass,action):  
  n1= random.uniform(0,1)
  n2= random.uniform(0,1)
  #print(n1, n2)
  if n1 > n2:
      randomiz(mass,action)
  else:
      highofhigh(mass,action)
      

epsilon1(mass,1)
print (address,price)
