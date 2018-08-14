"""
Extract all the texts inside <p> tag on the specified web page.
Put the scraped texts into a txt file
"""
from bs4 import BeautifulSoup
import urllib.request as req

url = "http://news.ltn.com.tw/news/life/breakingnews/2485588"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
links = soup.find_all("p")

file = open('scraping_7.txt', 'w')

for p in links:
	text = p.string
	file.write(str(text))