import requests
from bs4 import BeautifulSoup

import os
os.system("cls")


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_= "card-content")
for job_element in job_elements:
    title = job_element.find("h2", class_= "title")
    company = job_element.find("h3", class_= "subtitle")
    location = job_element.find("p", class_= "location")
    print(f"Job: {title.text.strip()}")
    print(f"Company: {company.text.strip()}")
    print(f"Location: {location.text.strip()}\n")


