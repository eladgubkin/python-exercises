def last(my_str):
    return my_str[-1]


def main():
    countries = ['Netherlands', 'Israel', 'England', 'Spain']
    countries.sort(key=last)
    print(countries)


print(main())