class FavoriteAnimal(object):

    def __init__(self):
        self.name = 'Vafel'
        self.age = 10

    def birthday(self):
        self.age += 1
        return self.age

    def get_age(self):
        return self.birthday()


def main():
    dog = FavoriteAnimal()
    print ' '.join([dog.name, 'is', str(dog.age), 'years old.',
                    '\nHappy birthday', dog.name + '.'
                    '\n' + dog.name, 'is now', str(dog.get_age()), 'years old.'])


if __name__ == '__main__':
    main()
