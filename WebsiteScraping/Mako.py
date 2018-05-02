from bs4 import BeautifulSoup
import requests
import csv
import sys


def write_to_csv(soup):
    csv_file = open('Mako.csv', 'w')

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


def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')

    source = requests.get('http://rcs.mako.co.il/rss/31750a2610f26110VgnVCM1000005201000aRCRD.xml').text

    soup = BeautifulSoup(source, 'lxml')

    write_to_csv(soup)


if __name__ == '__main__':
    main()
