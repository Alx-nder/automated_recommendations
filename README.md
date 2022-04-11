**OVERVIEW**  

This is an automated recommendation system which can work with small-scale web applications providing a few modifications. Being automated, the scripts coordinate the ETL process without much need for developer input.


**CODE**

**epsilon.py**

This script is the final part of the total data product. The recommendation is built to first recommend  A,B,C,D,...,Z (items to be recommended) equally. As soon as one item starts to outperforming the others (see update_pref.py), resources are shifted to start recommending that item more often. There is still a provision to show the other items. The alogrithm just starts to recommend them less. Altogether the apparently superior item is immediately acknowledged while minimizing inferior recommendations. 
N.B showing the 'inferior' items gives the system an oppurtunity to see, and adjust if an inferior item starts to do better (than the superior item).  


**update_pref.py**

This script ingests user (click) activity back into the database where that data will be incorporated (immediately) into the recommendation model - epsilon.py.


                                        load_user.py
Provided a relational database, this script loads and cleans and otherwise prepares data for the recommendation model. Preprocessing is done here also. 
This script creates python lists from data in the USER_PREF table of the database. 

HERE, THE tags (say specific locations or price tabs) are paired with number of times a particular user clicks on it. 
For example location_5=[a_location, interaction_count] LOOKS LIKE location_5=["Maryland",10]. 
This is done for all tags. 

Next, where applicable, the common tags are nested into a bigger list and the tally of the interactions appended to the end. 
For example global_tag[example_tag_1, example_tag_1,...example_tag_1, collective_interaction_count] LOOKS LIKE locations[["maryland",4],["Virginia",2],...["hawaii",0], 69].

Global tags are then nested into a final list for the recommendation algorithm to traverse and use.
For example final_list=[locations, prices ... any_other_global_tags, -1].
The -1 is used as an escape character. 
