import requests

resp=requests.get("https://reqres.in/api/users?page=2")

requests.

#print(resp)
#print(type(resp))
#print(dir(resp))

code=resp.status_code
#print(code)
assert code==200,"code doesn't match"

#print(resp.text)

#print(resp.content)

print(resp.json())

print(type(resp.headers))

print(resp.headers)
print(resp.cookies)
print(resp.encoding)
print(resp.url)

