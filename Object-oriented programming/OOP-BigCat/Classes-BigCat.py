class BigThing(object):

    def __init__(self, any_var):
        self.var = any_var

    def size(self):
        if isinstance(self.var, int):
            return self.var

        if isinstance(self.var, (str, list, dict)):
            return len(self.var)

        else:
            return 'Not one of these - [str, list, dict, int]'


class BigCat(BigThing):

    def __init__(self, any_var, weight):
        super(BigCat, self).__init__(any_var)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return 'Very fat'

        if self.weight > 15:
            return 'Fat'

        else:
            return 'OK'


def main():
    big_thing = BigThing('Oscar')
    big_cat = BigCat('Cat', 25)

    print(big_thing.size())
    print(big_cat.size())


if __name__ == '__main__':
    main()
