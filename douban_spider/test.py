import requests



url = "http://139.9.128.8:5555/random"

res = requests.get(url)
print(res.text)