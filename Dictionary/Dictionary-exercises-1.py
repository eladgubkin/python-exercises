prices = {'Banana': 10, 'Apple': 8, 'Bread': 7, 'Cheese': 20, 'Juice': 15}
shopping_cart = {'Banana': 2, 'Bread': 3, 'Cheese': 1, 'Orange': 13, 'Milk': 99}


def sum_of_cart(total):
    for key in shopping_cart.keys():

        if key not in prices.keys():
            print 'Sorry! {} is currently not available.'.format(key)

        elif key in prices.keys():
            total += prices.get(key) * shopping_cart.get(key)

    return 'Subtotal worth = {} shekels.'.format(total)


def main():
    total = 0
    print sum_of_cart(total)


if __name__ == '__main__':
    main()
