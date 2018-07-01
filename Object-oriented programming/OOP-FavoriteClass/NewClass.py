class FavoriteAnimal(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def set_name(self):
        name_check = input("Do you want to change the animal's name? [Yes] [No] ")
        if name_check.lower() == 'yes':
            self.__name = input('Enter the name here: ')

        elif name_check.lower() == 'no':
            self.__name = self.__name
            print("Very well, Your animal's name is still {}.".format(FavoriteAnimal.get_name(self)))
            quit()

        else:
            print('Invalid action - Try again')
            FavoriteAnimal.set_name(self)

    def __str__(self):
        print('\n{} is {} years old.'.format(FavoriteAnimal.get_name(self), FavoriteAnimal.get_age(self)))
        FavoriteAnimal.birthday(self)
        print('Happy birthday {}.'.format(FavoriteAnimal.get_name(self)))
        return '{} is now {} years old.\n'.format(FavoriteAnimal.get_name(self), FavoriteAnimal.get_age(self))
        # if last line is not return it will give a TypeError
