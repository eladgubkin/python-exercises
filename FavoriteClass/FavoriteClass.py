
class FavoriteAnimal:

    def __init__(self):
        self.name = 'Vafel'
        self.age = 10

    def birthday(self):
        self.age += 1
        return self.age

    def get_age(self):
        print 'Happy Birthday {} You are now {} years old'.format(self.name, self.birthday())


dog = FavoriteAnimal()
dog.get_age()

