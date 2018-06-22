def bit_counter(number, bits):
    while number != 0:
        bits += number & 1
        number = number >> 1
    return bits


def main():
    number = 7
    bits = 0
    print bit_counter(number, bits)


if __name__ == '__main__':
    main()
