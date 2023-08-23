#!C:\Users\Tyreek ALEXANDER\AppData\Local\Programs\Python\Python310\python.exe
print("content-type: text/html;\n\n")

import sys

sys.path.append(
    r"C:\Users\Tyreek ALEXANDER\AppData\Local\Programs\Python\Python310\Lib\site-packages"
)
import json
import cgi
import mysql.connector
import pandas as pd

# connecting to database
db = mysql.connector.connect(
    host="localhost", user="root", database="virttour", autocommit=True
)

# ## accept ajax body
form = cgi.FieldStorage()

# loads json the obj sent from js
js_postdata = json.loads(form.getvalue("message_py"))
location_pref = js_postdata["card_location"]
price_pref = int(js_postdata["card_price"])
current_user = js_postdata["username"]
listings_id = int(js_postdata["listing_id"])


query1 = "select * from user_pref"
pref_data = pd.read_sql(query1, db)
pref_data.set_index("username", inplace=True)

### a single record located at [col][row]
location_interaction = pref_data[location_pref][current_user]

# consilidating prices based on tabs of 1,000,000
if price_pref <= 1000000:
    price_pref = pref_data.columns[0]
elif price_pref > 1000000 and price_pref <= 2999999:
    price_pref = pref_data.columns[1]
else:
    price_pref = pref_data.columns[2]

price_interaction = pref_data[price_pref][current_user]

### updating the interaction
cursor = db.cursor()
# update count on the listing
query = f"update listings set listings_interaction = (listings_interaction+1) where id='{listings_id}'"
cursor.execute(query)

##using backquotes in the event of non-conformant field names
## updating preference data
query = f"update user_pref set `{location_pref}`={location_interaction+1},`{price_pref}`={price_interaction+1} where username='{current_user}'"
cursor.execute(query)
