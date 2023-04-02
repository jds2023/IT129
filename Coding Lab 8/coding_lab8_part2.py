import requests
from bs4 import BeautifulSoup

import os
os.system("cls")

URL = "https://www.scrapethissite.com/pages/simple/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id= "page")

web_scrapping2 = results.find_all("div", class_= "col-md-4 country")
for geographic_info in web_scrapping2:
    country = geographic_info.find("h3", class_= "country-name")
    capital = geographic_info.find("span", class_= "country-capital")
    print(country.text.strip())
    print(f"{capital.text.strip()}\n")
