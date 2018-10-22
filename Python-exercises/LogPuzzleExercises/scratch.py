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
    my_list = []
    with open(filename, 'r') as logo:
        for line in logo:
            python = line.find('/python')
            jpg = line.find('.jpg')
            if line[python:jpg + 4] != '':
                my_list.append('http://data.cyber.org.il' + line[python:jpg + 4])
        return sorted([item for item, count in collections.Counter(url_list).items() if count > 1])


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    urllib.urlretrieve(img_urls, dest_dir)
    i = 1
    os.remove('E:\code\Python2\LogPuzzleExercises\index.html')
    with open('E:\code\Python2\LogPuzzleExercises\index.html', 'a') as html_file:
        html_file.write('<html>')
        html_file.write('<body>')
        for thing in read_urls(sys.argv[1]):
            filename = str(i) + '.jpg'
            path5 = r"E:\code\Python2\LogPuzzleExercises\\" + filename
            html_file.write('<img src="' + thing + '">')
            i += 1
            download_images(thing, path5)
            html_file.write('</body>')
        html_file.write('</html>')
