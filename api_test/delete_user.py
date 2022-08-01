import requests

resp=requests.delete("https://reqres.in/api/users/2")

code=resp.status_code
print(code)

assert resp.status_code==204,"user deleted successfully"