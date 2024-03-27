import requests
url_1 = "https://reqres.in/api/users?page=2"
url_2 = "https://reqres.in/api/users"
url_3 = "https://reqres.in/api/users/23"
res = requests.get(url_1)
print(res.json())
res_2 = requests.post(url_2,{"name":"morpheus","job": "leader"})
print(res_2.json())
res_3 = requests.get(url_3)
print(res_3)