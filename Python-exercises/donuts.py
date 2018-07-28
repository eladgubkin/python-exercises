
def donuts(count):
    if count < 10:
        return 'Number of donuts:' + str(count)
    else:
        return 'Number of donuts: Too many mate'


print(donuts(int(input('Please enter number of donuts'))))
