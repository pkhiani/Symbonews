from bs4 import BeautifulSoup
import requests
from csv import writer

symbol = input("Enter a symbol you want to find the news for: ")

url = 'https://finviz.com/quote.ashx?t='

res = requests.get(url + symbol, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(res.text, "html.parser")

articles = soup.find_all("table", {"class": "fullview-news-outer"})

with open('news.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Link', 'Headline', 'Details','Source']
    csv_writer.writerow(headers)

    for newsElement in articles:
        rows = newsElement.find_all('tr')
        #print(rows)
        
        for row in rows:
            link = row.find("a", {"class":"tab-link-news"})['href']
            article_name = row.find("div", {"class":"news-link-left"}).get_text().strip()
            source = row.find("div", {"class":"news-link-right"}).get_text().strip()
            details = row.find('td').get_text().strip()
            csv_writer.writerow([link, article_name, details, source])