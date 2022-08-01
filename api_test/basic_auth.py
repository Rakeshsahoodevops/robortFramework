import requests

res=requests.get("http://the-internet.herokuapp.com/basic_auth",auth=('admin','admin'))

print(res.status_code)