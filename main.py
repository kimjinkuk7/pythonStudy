import requests

res = requests.get("https://www.naver.com")
print(res.text)