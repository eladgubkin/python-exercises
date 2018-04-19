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
    dog = FavoriteAnimal('Vafel', 10)
    print '{} is {} years old.'.format(dog.get_name(), dog.get_age())
    dog.birthday()
    print 'Happy birthday {}'.format(dog.get_name())
    print '{} is now {} years old.'.format(dog.get_name(), dog.get_age())


if __name__ == '__main__':
    main()
