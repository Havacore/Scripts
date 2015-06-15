import requests
import urllib
import wget
from bs4 import BeautifulSoup

page = requests.get("http://netrunnerdb.com/find/?q=jackson+howard")
data = page.text
soup = BeautifulSoup(data)

image_tag = soup.find("div", "card-image")

image_link = image_tag.find("img")['src']

full_image_link = "netrunnerdb.com" + image_link
print full_image_link
urllib.urlretrieve(full_image_link, "C:\Users\Jason\Documents\Scripts\jasckson_howard.png")

