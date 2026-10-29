import requests

# url="http://127.0.0.1:5000/api/applications"

# data={
#     "company_name": "TCS",
#     "job_role": "python developer",
#     "status":"Applied",
#     "applied_date":"2026-10-27"
# }
# response=requests.post(url,json=data)

# print("Status code:", response.status_code)
# print("Response:", response.text)

# url="http://127.0.0.1:5000/api/applications/1"

# data={
#     "status":"Interview"
# }

# response=requests.put(url,json=data)

# print("Status code:",response.status_code)
# print("response:",response.text)

# url= "http://127.0.0.1:5000/api/applications/9999"

# response=requests.delete(url)

# print("Status code:", response.status_code)
# print("Response:",response.text)

# url="http://127.0.0.1:5000/api/applications"

# data={
#     "company_name": "Infosys"

# }
# response=requests.post(url,json=data)

# print("Status code:",response.status_code)
# print("Response:",response.text)

#url = "http://127.0.0.1:5000/api/applications"

# data={
#       "company_name": "Infosys",
#       "job_role": "python developer",
#       "status":"Applied",
#       "applied_date":"2026-10-27"
#   }
# response=requests.post(url,json=data)

# print("Status code:", response.status_code)
# print("Response:", response.text)

# url = "http://127.0.0.1:5000/api/applications"

# response=requests.get(url)

# print("Status code:",response.status_code)
# print("Response:",response.text)

# url = "http://127.0.0.1:5000/api/applications"

# data={
#     "company_name":"Infosys",
#     "job_role":"Python Developer",
#     "status":'Interview'
# }

# response=requests.post(url,json=data)
# print("Status code:",response.status_code)
# print("Response:",response.text)

# url = "http://127.0.0.1:5000/api/applications"
# response=requests.get(url)

# print("Status code:",response.status_code)
# print("Applications:",response.json())


# url="http://127.0.0.1:5000/api/applications/1"

# data={
#     "status":"Selected"

# }
# response=requests.put(url,json=data)

# print("Status code:",response.status_code)
# print("Response:",response.json())

url= "http://127.0.0.1:5000/api/applications/5"

response=requests.delete(url)

print("Status code:", response.status_code)
print("Response:",response.json())

