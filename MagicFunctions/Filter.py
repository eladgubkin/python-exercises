# This should be done with filter()

# a function that receives a number
# and returns a list of all the smaller numbers that can be divided by 3


def func(given_number):
    result = []
    for y in range(1, given_number):
        if y % 3 == 0:
            result.append(y)
    return result


x = (lambda given_number: given_number)

z = [i for i in range(1, x(10)) if i % 3 == 0]


print z
print func(15)

