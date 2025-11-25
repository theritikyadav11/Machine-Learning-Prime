import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

# Create and open CSV file
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write column headers
    writer.writerow(["Quote", "Author", "Tags"])
    
    # Write data rows
    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        tags = ", ".join([tag.text for tag in q.find_all("a", class_="tag")])
        
        writer.writerow([text, author, tags])

print("Quotes saved successfully to quotes.csv")
