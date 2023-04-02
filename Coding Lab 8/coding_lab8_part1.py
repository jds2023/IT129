import requests
from bs4 import BeautifulSoup

import os
os.system("cls")

URL = "https://www.scrapethissite.com/pages/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id= "pages")

web_scrapping1 = results.find_all("div", class_= "page")
for information in web_scrapping1:
    title = information.find("h3", class_= "page-title")
    description = information.find("p", class_= "lead session-desc")
    print(title.text.strip())
    print(f"{description.text.strip()}\n")
