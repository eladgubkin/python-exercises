from bs4 import BeautifulSoup
import requests
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

source = requests.get('http://rss.walla.co.il/feed/22').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('Walla.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'date', 'link'])

for item in soup.find_all('item'):

    title = item.title.text
    print title

    date = item.pubdate.text
    print date

    link = item.link.text
    print link

    print ''

    csv_writer.writerow([title, date, link])

csv_file.close()
