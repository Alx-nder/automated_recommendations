#!C:\Program Files\Python310\python.exe
print("content-type: text/html;\n\n" )

import sys
sys.path.append(r'C:\Users\tyree\AppData\Roaming\Python\Python310\site-packages')

import json
import requests
import random

# string substitutions
# declaring te api version 1 or 2
api_version = 'v1'
# base url given by deentraland
api_base_url = f"https://api.decentraland.org/{api_version}"

# base url and id given by decentraland v2 to submit queries
graph_base_url="https://api.thegraph.com/subgraphs/name/decentraland/marketplace"
GRAPH_ID="QmaRXWMMB7qrKCVFYACaJ5iH9QcjT2oYYrBMfv5ECaK8tr"
# query attribute to request items from graph api
graph_query={
    "query":"""{
    nfts(first: 50, orderBy: searchOrderPrice, where:{ category: parcel, searchOrderStatus: open, searchOrderExpiresAt_gt: 1611082372 }) {
    parcel {
      id,
      
      x,
      y,
      owner{
        id,
      }
    }
    activeOrder {
      price,
      status
    }
    }
    }"""
}  

# using api to get maps with url parameters
map_png_endpoint_path= f"/map.png?center=23,-23&selected=23,-23&size=20&width=2048&height=2048"

# the final endpoint to communicate with
# v1_final_endpoint=f"{api_base_url}{}"

r = requests.post(graph_base_url,json=graph_query)

# print("############")
file=json.loads(r.text)

# parsed to only show the results 
parsed_response=file['data']['nfts']
a_nft=random.choice(parsed_response)


nft = a_nft['parcel']
nft_x=nft['x']
nft_y=nft['y']
nft_id=nft['id']

owner=nft["owner"]["id"]

pic_url=f"{api_base_url}/parcels/{nft_x}/{nft_y}/map.png"
nft_tour=f"https://play.decentraland.org/?position={nft_x},{nft_y}"
nft_price=int(a_nft["activeOrder"]["price"])/1000000000000000000000
nft_status=a_nft["activeOrder"]["status"]

final_json=[ nft_x,nft_y,nft_id,owner, pic_url,nft_tour,nft_price,nft_status]
print(json.dumps(final_json))

  
  