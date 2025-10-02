import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
#get the link
url = "https://www.ccny.cuny.edu/registrar/fall"
response = requests.get(url)

content = BeautifulSoup(response.content, "html.parser")
#print(content.title.text)

rows = []
for row in content.find_all("tr"):
    cells = [c.get_text(" ", strip=True) for c in row.find_all("td")]
    if len(cells) == 3:   # only rows with 3 columns
        rows.append(cells)
#set up frame     
df = pd.DataFrame(rows, columns=["date_str", "dow", "text"])
dates = []
dows = []
texts = []

#fill in the frame
for _, r in df.iterrows():
    date_str = r["date_str"]
    description = r["text"]
    if "-" in date_str:   #for multiple days
        try:
            start_str, end_day = date_str.replace("–", "-").split("-")
            start_date = datetime.strptime(start_str.strip() + " 2021", "%B %d %Y")
            end_date = start_date.replace(day=int(end_day.strip()))

            for n in range((end_date - start_date).days + 1):
                d = start_date + timedelta(days=n)
                dates.append(d)
                dows.append(d.strftime("%A"))
                texts.append(description)
        except:
            continue
    else: #single days
        try:
            d = datetime.strptime(date_str.strip() + " 2021", "%B %d %Y")
            dates.append(d)
            dows.append(d.strftime("%A"))
            texts.append(description)
        except:
            continue


calendar_df = pd.DataFrame({ "dow": dows,"text": texts}, index=pd.to_datetime(dates))
# Step 8. Sort by date and preview
calendar_df = calendar_df.sort_index()
calendar_df.head(10)
