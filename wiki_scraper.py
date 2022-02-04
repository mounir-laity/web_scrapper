# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_sovereign_states"
source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")
# On fait ça pour avoir le code html de la page dans un fichier pour facilement le visualiser
with open("wiki_file.html", "w+", encoding="utf-8") as file:
    file.write(source)
with open("countries.txt", "w+") as wiki_file:
    table = soup.find("table", class_="wikitable")
    lines = 0
    for row in table.tbody.find_all("tr"):
        try:
            span = row.td.span
            country = span.attrs["id"]
            country = country.replace("_", " ")
            wiki_file.write(country + "\n")
        except Exception:
            pass
        lines += 1
    wiki_file.write("There are " + str(lines) + " countries.")
