import requests
from bs4 import BeautifulSoup

# Step 1: Website URL
url = "https://www.bbc.com/news"

# Step 2: Send request
response = requests.get(url)

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find all headlines (h2 tags)
headlines = soup.find_all("h2")

# Step 5: Open file to save headlines
with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines:
        text = headline.get_text().strip()
        if text:   # Avoid empty lines
            print(text)
            file.write(text + "\n")

print("Headlines saved successfully!")