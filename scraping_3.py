"""
Scraping Beginner Level 3
- Extracting data using an API using urlencode and urllib.parse
"""
#!/usr/bin/python
# -*- coding: utf-8-*-

import urllib.request
import urllib.parse

API = "http://api.aoikujira.com/zip/xml/get.php"

values = {
	'fmt': 'xml',
	'zn': '6550874'
}

params = urllib.parse.urlencode(values)

url = API + "?" + params
print("url=", url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)

