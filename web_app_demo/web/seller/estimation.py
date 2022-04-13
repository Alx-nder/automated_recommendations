#!C:\Program Files\Python310\python.exe
print("content-type: text/html;\n\n" )

import sys
sys.path.append(r'C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages')
import mysql.connector as connection
import pandas as pd
from sklearn.linear_model import LinearRegression
import json

# connecting to database
db=connection.connect(
    host="localhost",
    user="root",
    database="virttour"
) 
query="select * from listings"

db_data= pd.read_sql(query,db)

predictors=["living_space","bathrooms","bedrooms","building_class","land", "age"]
outcome='price'

model = LinearRegression()
model.fit(db_data[predictors],db_data[outcome])

co_eff=[]
# print("Coefficients: ")
for name, coef in zip(db_data[predictors], model.coef_):
    # print(f" {name} : {coef}")
    co_eff.append(coef)

print(json.dumps(co_eff))