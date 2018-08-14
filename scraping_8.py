"""
Scrape texts using CSS selector
"""
from bs4 import BeautifulSoup

html = """
<html><body>
<div id="type1">
	<h1>aaaaa</h1>
	<ul class="items>
		<li>bbbbbbbbbbbbbbbbb</li>
		<li>ccccccccccccccccc</li>
		<li>ddddddddddddddddd</li>
	</ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")

h1 = soup.select_one("div#type1 > h1").string
print("h1 =", h1)

li_list = soup.select("div#type1 > ul.items > li")
for li in li_list:
	print("li =", li.string)
print("li =", li.string)