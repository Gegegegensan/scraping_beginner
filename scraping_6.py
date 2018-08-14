from bs4 import BeautifulSoup
import urllib.request as req

url = "http://news.ltn.com.tw/news/life/breakingnews/2485588"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

content = soup.find("p").string

print(content)