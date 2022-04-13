#!C:\Program Files\Python310\python.exe

import sys
sys.path.append(r'''C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages''')

import jwt
import requests
import json
import datetime

# all code contained in main
def main():
	# API key and your API secret issued from zoom
	API_KEY = 'P2VgBjzBSGmWExeDMPgHiQ'
	API_SEC = 'HzFTDkWetRJeo8TnKVE3q9aYXGQTpsIFPIp8'

	# api key and expiration time is needed for token generation
	currenttime= datetime.datetime.now()
	expiring = currenttime + datetime.timedelta(seconds=17) 
	#rounded off unix epoch time
	expiringfrmt = round(expiring.timestamp())


	headers={ 
		"alg": "HS256",
		"typ": "JWT"
		}
	payload ={
		"iss": API_KEY,
		"exp": expiringfrmt
	}

	encodedjwt= jwt.encode(payload,API_SEC,algorithm="HS256")

	# email of who is creating meeting
	email= "info.virttour@gmail.com"

	# endpoint provided by zoom api
	url='https://api.zoom.us/v2/users/{}/meetings'.format(email)
	header = {"authorization":"Bearer {}".format(encodedjwt)}
	date = datetime.datetime(2022,1,26,23,30).strftime("%Y-%M-%dT%H:%M:%SZ")

	# meeting details
	obj={"topic":"Live agent","starttime":date, "duration":30, "password":"12345"}

	# post method creates meeting -  the url with details and the authorization 
	createmeeting = requests.post(url,json=obj, headers= header)

	file = json.loads(createmeeting.text)
	print(file)
	join_url = file["join_url"]
	
	return f'\n here is your zoom meeting link <a href= {join_url} target=\"_blank\">{join_url}</a>\n'

# script to prevent the program from running when importing 
if __name__ == "__main__":
	main()	

	