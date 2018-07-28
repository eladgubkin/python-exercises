import random
CONTROL_TOWER_LOCATION = (4, 4)


class CrazyPlane:

    def __init__(self):
        self.__x = 0
        self.__y = 0

    def update_position(self):
        self.__x += random.randint(-1, 1)
        self.__y += random.randint(-1, 1)

    def get_position(self):
        return self.__x, self.__y

    def set_position(self, x, y):
        if (x, y) == CONTROL_TOWER_LOCATION:
            print('Location of the tower')
        elif x < 0 or y < 0:
            print('Illegal location')
        else:
            self.__x = x
            self.__y = y
            print('Position set')


class NormalPlane:

    def __init__(self):
        self.__x = 0
        self.__y = 0

    def update_position(self):
        self.__x += 1
        self.__y += 1

    def get_position(self):
        return self.__x, self.__y


def main():
    print('This main is not reached if the file is imported')


if __name__ == '__main__':
    main()
