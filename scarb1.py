import requests
from bs4 import BeautifulSoup
import csv

pagesc = requests.get('https://quotes.toscrape.com')
soup = BeautifulSoup(pagesc.text, "html.parser")



quotes = soup.findAll("span", class_="text")
authors = soup.findAll("small", class_="author")


file = open("scrabdot.csv", "w", newline='', encoding='utf-8')
writer = csv.writer(file)


writer.writerow(["QUOTES", "AUTHORS"])


for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])

file.close()




#for quote in quotes:
    #print(quote.text)
#for author in authors:
    #print(author.text)
