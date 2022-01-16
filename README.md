# recommendAlgo
variations in epsilon greedy algorithm

create tuples/lists for each parameter/feature to be recommended
nest tuple/list for count and other parameter like price etc
      
two part tupple for count and data
material, count>    wood, count
                    brick, count
price, count>       min, max, count
                    min, max, count
location, count>    loc1, count
                    loc2, count
run epsilon algo for recommendation
select random or fixed from db where data = foo in db
