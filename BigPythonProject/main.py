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
[nop <variable>] - No Operation: Simply does nothing!
[quit]
"""


def mov_function(user_input_list, var_dict):
    """Defines the variable to the given value"""
    try:
        command, variable, value = user_input_list
        variable = variable[:-1]

        if not variable.isdigit():
            if value and variable in var_dict:
                var_dict[variable] = var_dict[value]
                var_dict.pop(value)
            else:
                var_dict[variable] = int(value)
        else:
            print 'SyntaxError: cannot assign a number as a variable'
    except Exception as e:
        print 'Error:', e


def print_function(user_input_list, var_dict):
    """Prints out the value of the given variable"""
    try:
        command, variable = user_input_list

        if variable in var_dict:
            print var_dict[variable]
        else:
            print "NameError: name '{}' is not defined".format(variable)
    except Exception as e:
        print 'Error:', e


def add_function(user_input_list, var_dict):
    """Adds the given value to the variable"""
    try:
        command, variable, value = user_input_list
        variable = variable[:-1]

        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable) + int(value)
        else:
            print 'SyntaxError: cannot add to a variable which that not exist'
    except Exception as e:
        print 'Error:', e


def sub_function(user_input_list, var_dict):
    """Subtracts the given value from the variable"""
    try:
        command, variable, value = user_input_list
        variable = variable[:-1]

        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable) - int(value)
        else:
            print 'SyntaxError: cannot subtract from a variable that does not exist'
    except Exception as e:
        print 'Error:', e


def write_function(user_input_list, var_dict):
    """Writes the value of the variable to the given file name"""
    try:
        command, variable, filename = user_input_list
        variable = variable[:-1]

        if variable in var_dict:
            with open(filename, 'w') as write_file:
                write_file.write(str(var_dict[variable]))
        else:
            print "NameError: name '{}' is not defined".format(variable)
    except Exception as e:
        print 'Error:', e


def load_function(user_input_list, var_dict):
    """Loads the variable with the value inside the given file name"""
    try:
        command, variable, filename = user_input_list
        variable = variable[:-1]

        if variable in var_dict:
            with open(filename, 'r') as load_file:
                var_dict[variable] = int(load_file.read())
        else:
            print "NameError: name '{}' is not defined".format(variable)
    except Exception as e:
        print 'Error:', e


def mul_function(user_input_list, var_dict):
    """Multiplies the variable by the given value"""
    try:
        command, variable, value = user_input_list
        variable = variable[:-1]

        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable) * int(value)
        else:
            print 'SyntaxError: cannot multiply a variable that does not exist'
    except Exception as e:
        print 'Error:', e


def inc_function(user_input_list, var_dict):
    """Increases the variable always by 1"""
    try:
        command, variable = user_input_list

        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable) + 1
        else:
            print 'SyntaxError: cannot increase a variable that does not exist'
    except Exception as e:
        print 'Error:', e


def dec_function(user_input_list, var_dict):
    """Decreases the variable always by 1"""
    try:
        command, variable = user_input_list

        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable) - 1
        else:
            print 'SyntaxError: cannot decrease from variable that does not exist'
    except Exception as e:
        print 'Error:', e


def nop_function(user_input_list, var_dict):
    """Simply does nothing!"""
    command, variable = user_input_list
    if variable in var_dict:
        pass
    else:
        print 'SyntaxError: cannot do "No Operation" to a variable that does not exist'


def check_command(user_input, var_dict):
    user_input_list = user_input.split(' ')
    try:
        if user_input_list[0] == 'mov' and user_input_list[1][-1] == ',':
            mov_function(user_input_list, var_dict)

        elif user_input_list[0] == 'print':
            print_function(user_input_list, var_dict)

        elif user_input_list[0] == 'add' and user_input_list[1][-1] == ',':
            add_function(user_input_list, var_dict)

        elif user_input_list[0] == 'sub' and user_input_list[1][-1] == ',':
            sub_function(user_input_list, var_dict)

        elif user_input_list[0] == 'write' and user_input_list[1][-1] == ',':
            write_function(user_input_list, var_dict)

        elif user_input_list[0] == 'load' and user_input_list[1][-1] == ',':
            load_function(user_input_list, var_dict)

        elif user_input_list[0] == 'mul' and user_input_list[1][-1] == ',':
            mul_function(user_input_list, var_dict)

        elif user_input_list[0] == 'inc':
            inc_function(user_input_list, var_dict)

        elif user_input_list[0] == 'dec':
            dec_function(user_input_list, var_dict)

        elif user_input_list[0] == 'nop':
            nop_function(user_input_list, var_dict)

        elif user_input == 'quit':
            quit()

        elif len(user_input_list) == 1:
            print "NameError: name '{}' is not defined".format(user_input)

        else:
            print 'SyntaxError: invalid syntax'

    except Exception as e:
        print 'Error:', e


def main():
    var_dict = {}
    print available_commands()
    while True:
        user_input = raw_input('>>> ')
        check_command(user_input, var_dict)


if __name__ == '__main__':
    main()
