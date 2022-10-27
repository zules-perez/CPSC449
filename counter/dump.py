import requests

req = requests.get('http://localhost:5100')

print(req.text)

