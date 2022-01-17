import random

from matplotlib.pyplot import bar_label

def highofhigh(mass,action):
    max=mass[0][-1]
    maxi=0
    for x in range(0, len(mass)):
        if type(mass[x]) == "int":
            break
        if mass[x][-1] > max:
            max=mass[x][-1]
            maxi=x
    #running action to change values
    mass[maxi][-1]+=action
    newlist=mass[maxi]
    return newlist  

#prices min, max, count
p1=[7,10,0]
p2=[3,6,0]
p3=[1,2,0]

a1=['va',0]
a2=['md',1]
a3=['ja',0]

price=[p1,p2,p3,0]
address=[a1,a2,a3,1]
mass=[price,address]

def epsilon1(mass,action):
  print("Hello from a function")
  n1= random.random()
  n2= random.random()
  print(n1, n2)
  if n1 > n2:
      #random from the nested lists
      x=random.choice(mass)
      ######=random.c(x)
      #all except last ie count
      #running action to change values
      xl=0
      xl=x[-1]
      ####yl=0
      ####yl=y[-1]
      xl+= action
      ###yl+= action

      
      #print(y,type(y[-1]) )
  else:
    newlist = highofhigh(mass,action)
    print(newlist)



epsilon1(mass,1)

