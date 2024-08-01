import requests
from bs4 import BeautifulSoup
import csv

pagesc = requests.get('https://quotes.toscrape.com')
soup = BeautifulSoup(pagesc.text, "html.parser")

# Find all quotes and authors
quotes = soup.findAll("span", class_="text")
authors = soup.findAll("small", class_="author")

# Open CSV file for writing
file = open("scrabdot.csv", "w", newline='', encoding='utf-8')
writer = csv.writer(file)

# Write header row
writer.writerow(["QUOTES", "AUTHORS"])

# Write quotes and authors to the CSV file
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])

# Close the file
file.close()




#for quote in quotes:
    #print(quote.text)
#for author in authors:
    #print(author.text)
