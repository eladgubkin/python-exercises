#CR: All classes should always extend object like this: class MyClass(object)
class FavoriteAnimal:

    def __init__(self):
        self.name = 'Vafel'
        self.age = 10

    def birthday(self):
        self.age += 1
        return self.age

    def get_age(self):
        #CR: get_age should return the animal's age and you should do this print in the main() function
        print 'Happy Birthday {} You are now {} years old'.format(self.name, self.birthday())

#CR: main function, if __name__ == 'main', .......
#CR: Print age, then call birthday, then print new age
dog = FavoriteAnimal()
dog.get_age()

