import planes


def main():
    plane1 = planes.CrazyPlane()
    plane1.set_position(3, 4)
    print(plane1.get_position())


if __name__ == '__main__':
    main()