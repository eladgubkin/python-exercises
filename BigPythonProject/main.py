def available_commands():
    return """Available Commands:

[set <variable> <amount>]
[get <variable>]
[add <variable> <amount>]
[sub <variable> <amount>]
[write <variable> <file.txt>]
[load <variable> <file.txt>]
[quit]
"""


def set_function(user_input_list, var_dict):
    try:
        command, variable, value = user_input_list
        if not variable.isdigit():
            var_dict[variable] = int(value)
        else:
            print 'SyntaxError: cannot assign a number as a variable'
    except Exception as e:
        print 'Error:', e


def get_function(user_input_list, var_dict):
    try:
        command, variable = user_input_list
        if variable in var_dict:
            print var_dict[variable]
        else:
            print "NameError: name '{}' is not defined".format(variable)
    except Exception as e:
        print 'Error:', e


def add_function(user_input_list, var_dict):
    try:
        command, variable, value = user_input_list
        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable, 0) + int(value)
        else:
            print 'SyntaxError: cannot add to a variable which does not exist'
    except Exception as e:
        print 'Error:', e


def sub_function(user_input_list, var_dict):
    try:
        command, variable, value = user_input_list
        if variable in var_dict:
            var_dict[variable] = var_dict.get(variable, 0) - int(value)
        else:
            print 'SyntaxError: cannot subtract from a variable which does not exist'
    except Exception as e:
        print 'Error:', e


def write_function(user_input_list, var_dict):
    try:
        command, variable, filename = user_input_list
        if variable in var_dict:
            with open(filename, 'w') as write_file:
                write_file.write(str(var_dict[variable]))
        else:
            print "NameError: name '{}' is not defined".format(variable)
    except Exception as e:
        print 'Error:', e


def load_function(user_input_list, var_dict):
    try:
        command, variable, filename = user_input_list
        if variable in var_dict:
            with open(filename, 'r') as load_file:
                var_dict[variable] = int(load_file.read())
        else:
            print "NameError: name '{}' is not defined".format(variable)
    except Exception as e:
        print 'Error:', e


def check_command(user_input, var_dict):
    user_input_list = user_input.split(' ')

    if user_input_list[0] == 'set':
        set_function(user_input_list, var_dict)

    elif user_input_list[0] == 'get':
        get_function(user_input_list, var_dict)

    elif user_input_list[0] == 'add':
        add_function(user_input_list, var_dict)

    elif user_input_list[0] == 'sub':
        sub_function(user_input_list, var_dict)

    elif user_input_list[0] == 'write':
        write_function(user_input_list, var_dict)

    elif user_input_list[0] == 'load':
        load_function(user_input_list, var_dict)

    elif user_input == 'quit':
        quit()

    else:
        print "NameError: name '{}' is not defined".format(user_input)


def main():
    var_dict = {}
    print available_commands()
    while True:
        user_input = raw_input('>>> ')
        check_command(user_input, var_dict)


if __name__ == '__main__':
    main()
