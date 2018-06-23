def bit_counter(number):
    bits = 0
    while number != 0:
        bits += number & 1
        number = number >> 1
    return bits


def main():
    number = 7
    print bit_counter(number)


if __name__ == '__main__':
    main()
