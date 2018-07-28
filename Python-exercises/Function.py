def f(x, y):
    return x * y


print(f(5, 6))


def f_1(x, y):
    if y == 0:
        print('Illegal')
    else:
        return x / y


print(f_1(100, 5))