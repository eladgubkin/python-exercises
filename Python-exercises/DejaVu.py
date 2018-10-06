__author__ = 'Eladox'
# The program asks the user to insert a 5 digit number.
# The program prints:
# The actual number.
# Every digit of the number with commas unless its the end of the number.
# Entire sum of the number.
# PS : If user didn't enter a 5 digit number, the program will not collapse.
# Use Proper division of code, PEP8 and checking functions by assert.


def check_number():
    """If user entered an integer it will check if user_input is 5 digits exactly.
    If user didn't entered an integer, The loop will start again until user will enter
    a 5 digits integer
    """
    tries = 0
    input_int = 0

    while tries == 0:
        try:
            user_input = int(input('Please insert a 5 digit number:\n'))
            if len(str(user_input)) == 5:
                input_int += user_input
                tries = tries + 1
        except ValueError:
            tries = tries + 0
    return input_int


def print_number(input_int):
    """Prints out:
                #The number itself.
                #Every digit of the number with a comma unless its the end of the number.
                #Sum of the number.
    """
    print('You entered the number:', input_int)
    string = str(input_int)
    var = string[0] + ',' + string[1] + ',' + \
        string[2] + ',' + string[3] + ',' + string[4]
    print('The digits of the number are: {}'.format(var))
    print('The entire sum of this number is:', sum(int(num) for num in string))


print_number(check_number())
