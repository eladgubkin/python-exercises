def factorial(x):
    if x == 5:
        return 1 * 2 * 3 * 4 * 5


x = int(input('enter a number'))
print(factorial(x))


def beep(string):
    string = ''
    string = string + 'beep!'
    return string


string = input('Please enter a string')
print(beep(string))


def mul_2nums(x, y):
    z = x * y
    if z < 0:
        return 0
    else:
        return z

x = int(input('Enter a number'))
y = int(input('Enter another number'))
print(mul_2nums(x, y))
