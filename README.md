**OVERVIEW**
This is an automated recommendation system which can work with small-scale web applications providing a few modifications. Being automated, the scripts coordinate the ETL process without much need for developer input.

There are three parts

**CODE**
**epsilon.py**
This script is the final part of the total data product. The recommendation is built to first recommend  A,B,C,D,...,Z (items to be recommended) equally. As soon as one item starts to outperforming the others (see update_pref.py), resources are shifted to start recommending that item more often. There is still a provision to show the other items. The alogrithm just starts to recommend them less. Altogether the apparently superior item is immediately acknowledged while minimizing inferior recommendations. 
N.B showing the 'inferior' items gives the system an oppurtunity to see, and adjust if an inferior item starts to do better (than the superior item).  


**update_pref.py**
This script ingests user (click) activity back into the database where that data will be incorporated (immediately) into the recommendation model - epsilon.py.


**load_user.py**
Provided a relational database, this script loads and cleans and otherwise prepares data for the recommendation model. Preprocessing is done here also. For example: float values that are spread out are consolidated. 

create lists for each parameter/feature to be recommended
nest list for count and other parameter like price etc
      
two part list for count and data
material, count>    wood, count
                    brick, count
price, count>       min, max, count
                    min, max, count
location, count>    loc1, count
                    loc2, count
run epsilon algo for recommendation
        generate 2 random numbers between 0 and 1
        if n1<'n2' randomly select from options
        if n1>='n2' select highest count  
select random or fixed from db where data = foo in db

this does not ask what you are interested in, rather, it finds out

hover could determine if specs are as important as looks and more
offer a reset

create db for interactions tied to user
print array

select all values in certain coloumn
        add interaction 
this is a list
nest this list

for each user, 
        append interaction to  element in list 
        sum the interactions per similar column group 
        append interaction per group

add p value as a final test

