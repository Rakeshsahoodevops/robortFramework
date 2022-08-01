import requests
import json

payload={
    "name": "API"
}


resp=requests.patch("https://reqres.in/api/users/2",data=payload)
print(resp)
print(resp.json())
print(resp.headers.get("Content-type"))
assert (resp.json())['name']=='API'