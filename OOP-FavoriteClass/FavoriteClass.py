from NewClass import FavoriteAnimal


def main():
    animal = FavoriteAnimal('Vafel', 10)
    # animal prints out __str__
    print animal
    animal.set_name()
    print animal


if __name__ == '__main__':
    main()
