from stack import Stack


def available_commands():
    return """Available Commands:

[mov <variable>, <amount>] - Defines the variable to the given value
[print <variable>] - Prints out the value of the given variable
[add <variable>, <amount>] - Adds the given value to the variable
[sub <variable>, <amount>] - Subtracts the given value from the variable
[write <variable>, <file.txt>] - Writes the value of the variable to the given file name
[load <variable>, <file.txt>] - Loads the variable with the value inside the given file name
[mul <variable>, <amount>] - Multiplies the variable by the given value
[inc <variable>] - Increases the variable always by 1
[dec <variable>] - Decreases the variable always by 1
[nop] - No Operation: Simply does nothing!
[push <variable/value>] - Pushes the value to the stack
[pop <variable>] - Pops the value from the stack
[quit]
"""


def mov_function(params, var_dict):
    """Defines the variable to the given value"""
    try:
        variable, value = params

        if not variable.isdigit():
            if value in var_dict:
                var_dict[variable] = var_dict[value]
            else:
                var_dict[variable] = int(value)
        else:
            print 'SyntaxError: cannot assign a number as a variable'
    except Exception as e:
        print 'Error:', e


def print_function(params, var_dict):
    """Prints out the value of the given variable"""
    try:
        variable, = params

        if variable in var_dict:
            print var_dict[variable]
        else:
            print "NameError: name '{}' is not defined".format(variable)
    except Exception as e:
        print 'Error:', e


def add_function(params, var_dict):
    """Adds the given value to the variable"""
    try:
        variable, value = params

        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable) + int(value)
        else:
            print 'SyntaxError: cannot add to a variable which that not exist'
    except Exception as e:
        print 'Error:', e


def sub_function(params, var_dict):
    """Subtracts the given value from the variable"""
    try:
        variable, value = params

        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable) - int(value)
        else:
            print 'SyntaxError: cannot subtract from a variable that does not exist'
    except Exception as e:
        print 'Error:', e


def write_function(params, var_dict):
    """Writes the value of the variable to the given file name"""
    try:
        variable, filename = params

        if variable in var_dict:
            with open(filename, 'w') as write_file:
                write_file.write(str(var_dict[variable]))
        else:
            print "NameError: name '{}' is not defined".format(variable)
    except Exception as e:
        print 'Error:', e


def load_function(params, var_dict):
    """Loads the variable with the value inside the given file name"""
    try:
        variable, filename = params

        if variable in var_dict:
            with open(filename, 'r') as load_file:
                var_dict[variable] = int(load_file.read())
        else:
            print "NameError: name '{}' is not defined".format(variable)
    except Exception as e:
        print 'Error:', e


def mul_function(params, var_dict):
    """Multiplies the variable by the given value"""
    try:
        variable, value = params

        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable) * int(value)
        else:
            print 'SyntaxError: cannot multiply a variable that does not exist'
    except Exception as e:
        print 'Error:', e


def inc_function(params, var_dict):
    """Increases the variable always by 1"""
    try:
        variable, = params

        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable) + 1
        else:
            print 'SyntaxError: cannot increase a variable that does not exist'
    except Exception as e:
        print 'Error:', e


def dec_function(params, var_dict):
    """Decreases the variable always by 1"""
    try:
        variable, = params

        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable) - 1
        else:
            print 'SyntaxError: cannot decrease from variable that does not exist'
    except Exception as e:
        print 'Error:', e


def nop_function():
    """Simply does nothing!"""
    pass


def push_function(params, stack, var_dict):
    """Pushes the value to the stack"""
    try:
        variable, = params

        if variable in var_dict:
            stack.push(var_dict[variable])
        elif variable.isdigit():
            stack.push(int(variable))

        else:
            print "NameError: name '{}' is not defined".format(variable)
    except Exception as e:
        print 'Error:', e


def pop_function(params, stack, var_dict):
    """Pops the value from the stack"""
    try:

        variable, = params
        if not variable.isdigit():
            var_dict[variable] = stack.pop()
        else:
            print 'SyntaxError: cannot pop to a number'
    except Exception as e:
        print 'Error:', e


def check_command(user_input, var_dict, stack):
    if user_input.find(' ') == -1:
        command = user_input
        params = []
    else:
        command = user_input[:user_input.find(' ')]
        params = user_input[user_input.find(' ')+1:].split(', ')

    try:
        if command == 'mov':
            mov_function(params, var_dict)

        elif command == 'print':
            print_function(params, var_dict)

        elif command == 'add':
            add_function(params, var_dict)

        elif command == 'sub':
            sub_function(params, var_dict)

        elif command == 'write':
            write_function(params, var_dict)

        elif command == 'load':
            load_function(params, var_dict)

        elif command == 'mul':
            mul_function(params, var_dict)

        elif command == 'inc':
            inc_function(params, var_dict)

        elif command == 'dec':
            dec_function(params, var_dict)

        elif command == 'nop':
            nop_function()

        elif command == 'push':
            push_function(params, stack, var_dict)

        elif command == 'pop':
            pop_function(params, stack, var_dict)

        elif command == 'quit':
            quit()

        else:
            print 'SyntaxError: invalid syntax'

    except Exception as e:
        print 'Error:', e


def main():
    var_dict = {}
    stack = Stack()

    print available_commands()
    while True:
        user_input = raw_input('>>> ')
        check_command(user_input, var_dict, stack)


if __name__ == '__main__':
    main()
