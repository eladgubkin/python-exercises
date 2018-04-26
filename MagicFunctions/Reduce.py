# This should be done using reduce()

# a function that receives a number
# and returns the sum of the given number
# 104 -> 5


def f(num):
    numList = [int(i) for i in str(num)]
    return sum(numList)


print f(104)


num = sum(int(i) for i in str(44))

print num
