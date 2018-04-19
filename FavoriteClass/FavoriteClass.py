class FavoriteAnimal(object):

    def __init__(self):
        self.name = 'Vafel'
        self.age = 10

    def birthday(self):
        self.age += 1
        # birthday() shouldn't return anything, it just increases the age
        return self.age

    def get_age(self):
        #CR: get_age() should just return the age
        return self.birthday()

    
def main():
    dog = FavoriteAnimal()
    #CR: Use format() for stuff like this, and multiple prints is OK
    print ' '.join([dog.name, 'is', str(dog.age), 'years old.',
                    '\nHappy birthday', dog.name + '.'
                    '\n' + dog.name, 'is now', str(dog.get_age()), 'years old.'])


if __name__ == '__main__':
    main()
