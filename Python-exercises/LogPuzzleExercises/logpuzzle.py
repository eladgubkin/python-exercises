import collections
import urllib
import os
import sys


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    url_list = []
    with open(filename, 'r') as logo:
        for line in logo:
            python, jpg = line.find('/python'), line.find('.jpg')
            if line[python:jpg+4] != '':
                url_list.append('http://data.cyber.org.il' + line[python:jpg+4])
        var = sorted([item for item, count in collections.Counter(url_list).items() if count > 1])  # delete duplicates
        return sorted(var, key=lambda u: u[-8:-4])  # [-13:-9] if need to sort on the first key


def download_images(img_urls, dest_dir):
    urllib.urlretrieve(img_urls, dest_dir)


def main():
    i = 0
    os.remove('E:\code\Python2\LogPuzzleExercises\index.html')
    with open('E:\code\Python2\LogPuzzleExercises\index.html', 'a') as html_file:
        html_file.write('<html>')
        html_file.write('<body>')
        for thing in read_urls(sys.argv[2]):    # sys.argv[1] for 'gvahim' picture. [2] for success
            filename_1 = 'img' + str(i) + '.jpg'
            path5 = r"E:\code\Python2\LogPuzzleExercises\images\\" + filename_1
            html_file.write('<img src="' + thing + '">')
            i += 1
            download_images(thing, path5)
        html_file.write('</body>')
        html_file.write('</html>')


if __name__ == '__main__':
    main()
