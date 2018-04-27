from bs4 import BeautifulSoup
import requests
import csv
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')

source = requests.get('http://www.ynet.co.il/Integration/StoryRss1854.xml').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('ynet_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'date', 'link'])

for article in soup.find_all('item'):

    headline = article.category.text
    print headline

    summary = article.title.text
    print summary

    date = article.pubdate.text
    print date

    link = article.guid.text
    print link

    print ''

    csv_writer.writerow([headline, summary, date, link])

csv_file.close()
