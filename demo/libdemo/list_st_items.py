import requests
from bs4 import BeautifulSoup
from datetime import datetime

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text, "lxml-xml")

for t in bs.find_all("item"):
     pubDate = t.find("pubDate").text[5:16]
     print(t.find('title').text.strip())
     age =(datetime.now() - datetime.strptime(pubDate,'%d %b %Y')).days
     print(age)


