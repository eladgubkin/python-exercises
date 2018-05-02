import csv


class Website(object):

    def __init__(self, csv1, csv2, csv3):
        self.csv1 = csv1
        self.csv2 = csv2
        self.csv3 = csv3

    def write_to_html(self, html_output, data):

        csv_files = [self.csv1, self.csv2, self.csv3]

        for csv_file in csv_files:

            with open(csv_file, 'r') as data_file:
                csv_data = csv.DictReader(data_file)

                for line in csv_data:
                    if line['date'] == '':
                        break
                    else:
                        data.append('{} - <a href="{}">{}</a>'
                                    .format(line['date'], line['link'], line['title']))

            html_output += '<p> <b>This site has: {} new articles</b>.</p>'.format(len(data))

            html_output += '\n<ul>'

            for name in data:
                html_output += '\n\t<li>{}</li>'.format(name)

            html_output += '\n</ul>'

            with open('index.html', 'w') as html_file:
                html_file.write('<head> <h1>Awesome site of news</h1> </head>')
                html_file.write(html_output)
                data = []


def main():
    html_output = ''
    data = []

    website = Website('NewYorkTimes.csv', 'Walla.csv', 'Ynet.csv')
    website.write_to_html(html_output, data)


if __name__ == '__main__':
    main()
