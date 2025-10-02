import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = "https://www.ccny.cuny.edu/registrar/fall"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
#print(soup.title.text)
