"""
1. Extracting the text based on the specified id
"""

from bs4 import BeautifulSoup

html="""
<html><body>
	<h1 id="title">what is scraping?</h1>
	<p id="body">extracting data from a web page</h1>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

title = soup.find(id="title")
body = soup.find(id="body")

print("#title=" + title.string)
print("#body=" + body.string)
