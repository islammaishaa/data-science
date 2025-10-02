import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = "https://www.ccny.cuny.edu/registrar/fall"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
#print(soup.title.text)

rows = []
for row in soup.find_all("tr"):
    cells = [c.get_text(" ", strip=True) for c in row.find_all("td")]
    if len(cells) == 3:   
        rows.append(cells)
