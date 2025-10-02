import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = "https://www.ccny.cuny.edu/registrar/fall"
response = requests.get(url)

content = BeautifulSoup(response.content, "html.parser")
#print(content.title.text)

rows = []
for row in content.find_all("tr"):
    cells = [c.get_text(" ", strip=True) for c in row.find_all("td")]
    if len(cells) == 3:   # only rows with 3 columns
        rows.append(cells)
     
df = pd.DataFrame(rows, columns=["date_str", "dow", "text"])
dates = []
dows = []
texts = []

for _, r in df.iterrows():
    date_str = r["date_str"]
    description = r["text"]
    try:
        d = datetime.strptime(date_str.strip() + " 2021", "%B %d %Y")
        dates.append(d)
        dows.append(d.strftime("%A"))
        texts.append(description)
    except:
        continue

calendar_df = pd.DataFrame({
    "dow": dows,
    "text": texts
}, index=pd.to_datetime(dates))

# Step 8. Sort by date and preview
calendar_df = calendar_df.sort_index()
calendar_df.head(10)
