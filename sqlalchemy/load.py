import pandas as pd
import sqlalchemy as db

db_conn = db.create_engine("mysql://root:@localhost:3306/virttour")

# get the locations
house_locations = pd.read_sql("select house_location from listings", db_conn)
house_locations = list(set(house_locations["house_location"].tolist()))

clicks = pd.read_sql("select * from user_pref", db_conn)
print(clicks)
