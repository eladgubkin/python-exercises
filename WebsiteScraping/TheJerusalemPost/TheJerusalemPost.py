from bs4 import BeautifulSoup
import requests
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

source = requests.get('https://www.jpost.com/Rss/RssFeedsHeadlines.aspx').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('TheJerusalemPost.csv', 'w')

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
