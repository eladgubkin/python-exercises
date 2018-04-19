class FavoriteAnimal(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    
def main():
    for animal in FavoriteAnimal('Vafel', 10), FavoriteAnimal('Oscar', 4):
        print '{} is {} years old.'.format(animal.get_name(), animal.get_age())
        animal.birthday()
        print 'Happy birthday {}'.format(animal.get_name())
        print '{} is now {} years old.\n'.format(animal.get_name(), animal.get_age())


if __name__ == '__main__':
    main()
