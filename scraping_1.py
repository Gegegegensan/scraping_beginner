"""
Scraping Beginner Level 1
- Download an image from a URL
"""

import urllib.request

url = "" # a url for an image starting from http or https
savename = "demo.png"

urllib.request.urlretrieve(url, savename)
print("Successfully saved!")