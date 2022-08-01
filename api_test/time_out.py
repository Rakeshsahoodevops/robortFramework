import requests

resp=requests.get("https://httpbin.org/delay/3",timeout=5)
print(resp.status_code)