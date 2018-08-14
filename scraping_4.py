"""
Extracting the text based on the specified html tags
"""

from bs4 import BeautifulSoup

html = """
<html><body>
	<h1>what is scraping</h1>
	<p>to analyze web pages</p>
	<p>extract the pages you specify</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)