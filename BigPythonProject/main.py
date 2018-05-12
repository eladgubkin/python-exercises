from stack import Stack
import sys


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


class AsmException(Exception):
    pass


def mov_function(params, var_dict):
    """Defines the variable to the given value"""
    try:
        variable, value = params
    except ValueError:
        raise AsmException('SyntaxError: mov <variable>, <value>')

    if not variable.isdigit():
        if value in var_dict:
            var_dict[variable] = var_dict[value]
        else:
            var_dict[variable] = int(value)
    else:
        raise AsmException('SyntaxError: cannot assign a number as a variable')


def print_function(params, var_dict):
    """Prints out the value of the given variable"""
    try:
        variable, = params
    except ValueError:
        raise AsmException('SyntaxError: print <variable>')

    try:
        print var_dict[variable]
    except KeyError:
        raise AsmException("NameError: name '{}' is not defined".format(variable))


def add_function(params, var_dict):
    """Adds the given value to the variable"""
    try:
        variable, value = params
    except ValueError:
        raise AsmException('SyntaxError: add <variable>, <value>')

    try:
        var_dict[variable] += int(value)
    except KeyError:
        raise AsmException('SyntaxError: cannot add to a variable which that not exist')


def sub_function(params, var_dict):
    """Subtracts the given value from the variable"""
    try:
        variable, value = params
    except ValueError:
        raise AsmException('SyntaxError: sub <variable>, <value>')

    try:
        var_dict[variable] -= int(value)
    except KeyError:
        raise AsmException('SyntaxError: cannot subtract from a variable which that not exist')


def write_function(params, var_dict):
    """Writes the value of the variable to the given file name"""
    try:
        variable, filename = params
    except ValueError:
        raise AsmException('SyntaxError: write <variable>, <filename>')

    try:
        with open(filename, 'w') as write_file:
            write_file.write(str(var_dict[variable]))
    except KeyError:
        raise AsmException("NameError: name '{}' is not defined".format(variable))


def load_function(params, var_dict):
    """Loads the variable with the value inside the given file name"""
    try:
        variable, filename = params
    except ValueError:
        raise AsmException('SyntaxError: load <variable>, <filename>')

    with open(filename, 'r') as load_file:
        var_dict[variable] = int(load_file.read())


def mul_function(params, var_dict):
    """Multiplies the variable by the given value"""
    try:
        variable, value = params
    except ValueError:
        raise AsmException('SyntaxError: mul <variable>, <value>')

    try:
        var_dict[variable] *= int(value)
    except KeyError:
        raise AsmException('SyntaxError: cannot multiply to a variable which that not exist')


def inc_function(params, var_dict):
    """Increases the variable always by 1"""
    try:
        variable, = params
    except ValueError:
        raise AsmException('SyntaxError: inc <variable>')

    try:
        var_dict[variable] += 1
    except KeyError:
        raise AsmException('SyntaxError: cannot increase a variable that does not exist')


def dec_function(params, var_dict):
    """Decreases the variable always by 1"""
    try:
        variable, = params
    except ValueError:
        raise AsmException('SyntaxError: dec <variable>')

    try:
        var_dict[variable] -= 1
    except KeyError:
        raise AsmException('SyntaxError: cannot decrease from a variable that does not exist')


def nop_function():
    """Simply does nothing!"""
    pass


def push_function(params, stack, var_dict):
    """Pushes the value to the stack"""
    try:
        variable, = params
    except ValueError:
        raise AsmException('SyntaxError: push <variable>/<value>')

    if variable in var_dict:
        stack.push(var_dict[variable])

    elif variable.isdigit():
        stack.push(int(variable))

    else:
        raise AsmException("NameError: name '{}' is not defined".format(variable))


def pop_function(params, stack, var_dict):
    """Pops the value from the stack"""
    try:
        variable, = params
    except ValueError:
        raise AsmException('SyntaxError: pop <variable>')

    if not variable.isdigit():
        var_dict[variable] = stack.pop()

    else:
        raise AsmException('SyntaxError: cannot pop to a number')


def execute_command(user_input, var_dict, stack):
    if user_input.find(' ') == -1:
        command = user_input
        params = []
    else:
        command = user_input[:user_input.find(' ')]
        params = user_input[user_input.find(' ')+1:].split(', ')

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
        raise AsmException('SyntaxError: invalid command')


def main():
    var_dict = {}
    stack = Stack()

    filename = None
    try:
        _, filename = sys.argv
    except ValueError:
        pass

    if filename is not None:
        with open(filename, 'r') as input_file:
            lines = [x.strip() for x in input_file.readlines()]
            try:
                for line in lines:
                    execute_command(line, var_dict, stack)
            except AsmException as e:
                print e.message

    else:
        print available_commands()
        while True:
            user_input = raw_input('>>> ')
            try:
                execute_command(user_input, var_dict, stack)
            except AsmException as e:
                print e.message


if __name__ == '__main__':
    main()
