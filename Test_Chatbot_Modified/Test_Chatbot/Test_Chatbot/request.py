import requests

dat=requests.get("https://reqres.in/api/users")

print(data.text)