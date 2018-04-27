import urllib
import sys


def download_text():
    urllib.urlretrieve('http://www.ynet.co.il/Integration/StoryRss1854.xml',
                       r'E:\code\GitHub\python-exercises\ynetTitle\ynetText.xml')


def finding_text(new_text_list, text):
    title_start = text.find('<title>')
    title_end = text.find('</title>')

    new_text_list.append(text[title_start:title_end+8])


def main():
    download_text()
    xml_file, new_text_file = sys.argv[1], sys.argv[2]

    with open(xml_file, 'r') as ynet_text:
        text = ynet_text.read()

    new_text_list = []
    finding_text(new_text_list, text)

    with open(new_text_file, 'w') as ynet_new_text:
        ynet_new_text.write(''.join(new_text_list))


if __name__ == '__main__':
    main()
