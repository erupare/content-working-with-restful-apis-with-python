import requests

# url for all requests, do not change
URL = "http://127.0.0.1:5000"

# Scooby Doo is not a looney toons character, delete him from contacts
response = requests.delete("http://127.0.0.1:5000/api/contacts/3")
print("Status Code: %s" % response.status_code)
print("Contact List: %s" % response.text)