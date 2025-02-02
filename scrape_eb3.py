import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://immigrationroad.com/visa-bulletin/visa-bulletin-by-preference.php?vb-country=ROW&vb-preference=EB3"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}


response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")


table = soup.find("table")

if table:
    
    rows = []
    for tr in table.find_all("tr"):
        cells = tr.find_all("td")
        row = [cell.text.strip() for cell in cells]
        if row:
            rows.append(row)

    if len(rows) > 0:
        headers = rows[0]  # First row becomes headers
        rows = rows[1:]  # Remaining rows are data
    else:
        print(" No data found in the table.")
        exit()

    # Create a DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # Save to CSV
    df.to_csv("eb3_visa_bulletin.csv", index=False)

    print("Table successfully extracted and saved as 'eb3_visa_bulletin.csv'")
else:
    print(" No table found. Check website structure.")
