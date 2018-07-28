import sys
import os
PATH = 1


def main():
    directory = sys.argv[PATH]
    if os.path.isfile(directory):
        with open(directory, 'r') as input_file:
            for line in input_file:
                print(line,)
    else:
        print('oh okay..')


if __name__ == '__main__':
    main()