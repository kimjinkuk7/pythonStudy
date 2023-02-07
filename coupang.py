from bs4 import BeautifulSoup as BS
import requests as req

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
res = req.get(url, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
})
soup = BS(res.text, "html.parser")

arr = soup.select("div.name")
for a in arr:
    print(a.get_text(strip=True))

# arr = [a.get_text(strip=True) for a in soup.select("div.name")]
# print(arr)