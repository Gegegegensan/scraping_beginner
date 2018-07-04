"""
Scraping Beginner Level 2
- Download an image from a URL using .urlopen and open()
"""

import urllib.request

url = "" # a url for an image starting from http or https
savename = "demo_2.png"

mem = urllib.request.urlopen(url).read()

with open(savename, mode="wb") as f: # w = write, b = binary
	f.write(mem) # save a file for the downloaded binary data
	print("Successfully save!")