"""
Extract all the texts inside <p> tag on the specified web page.
Put the scraped texts into a txt file
"""
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://mojim.com/twy100012x54x6"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
links = soup.find_all("dd")

file = open('scraping_9.txt', 'w')

for d in links:
	text = d.string
	file.write(str(text))