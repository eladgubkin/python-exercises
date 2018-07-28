import sys


def main():
    with open(sys.argv[1], 'r') as input_file:
        for line in input_file:
            print(line,)


if __name__ == '__main__':
    main()
