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


def set_function(user_input_list, d):
    if len(user_input_list) == 3 and not user_input_list[1].isdigit() and user_input_list[2].isdigit():
        d.update({user_input_list[1]: int(user_input_list[2])})
    else:
        print 'SyntaxError: invalid syntax'


def get_function(user_input_list, d):
    if len(user_input_list) == 2:
        try:
            print d[user_input_list[1]]
        except KeyError:
            print "NameError: name '{}' is not defined".format(user_input_list[1])
    else:
        print 'SyntaxError: invalid syntax'


def add_function(user_input_list, d):
    if user_input_list[1] in d:
        if len(user_input_list) == 3 and not user_input_list[1].isdigit() and user_input_list[2].isdigit():
            d[user_input_list[1]] = d.get(user_input_list[1], 0) + int(user_input_list[2])
        else:
            print 'SyntaxError: invalid syntax'
    else:
        print "NameError: name '{}' is not defined".format(user_input_list[1])


def sub_function(user_input_list, d):
    if user_input_list[1] in d:
        if len(user_input_list) == 3 and not user_input_list[1].isdigit() and user_input_list[2].isdigit():
            d[user_input_list[1]] = d.get(user_input_list[1], 0) - int(user_input_list[2])
        else:
            print 'SyntaxError: invalid syntax'
    else:
        print "NameError: name '{}' is not defined".format(user_input_list[1])


def write_function(user_input_list, d):
    if len(user_input_list) == 3:
        if user_input_list[1] in d and user_input_list[2][-4:] == '.txt':
            with open(user_input_list[2], 'w') as write_file:
                write_file.write(str(d[user_input_list[1]]))
        else:
            print "Error: Can't find file name"
    else:
        print 'SyntaxError: invalid syntax'


def load_function(user_input_list, d):
    if len(user_input_list) == 3:
        if user_input_list[1] in d:
            try:
                with open(user_input_list[2], 'r') as load_file:
                    d[user_input_list[1]] = int(load_file.read())
            except IOError:
                print "Could not read file:", user_input_list[2]
        else:
            print "NameError: name '{}' is not defined".format(user_input_list[1])
    else:
        print 'SyntaxError: invalid syntax'


def check_command(user_input, d):
    user_input_list = user_input.split(' ')

    if user_input_list[0] == 'set':
        set_function(user_input_list, d)

    elif user_input_list[0] == 'get':
        get_function(user_input_list, d)

    elif user_input_list[0] == 'add':
        add_function(user_input_list, d)

    elif user_input_list[0] == 'sub':
        sub_function(user_input_list, d)

    elif user_input_list[0] == 'write':
        write_function(user_input_list, d)

    elif user_input_list[0] == 'load':
        load_function(user_input_list, d)

    elif user_input == 'quit':
        quit()

    else:
        print "NameError: name '{}' is not defined".format(user_input)


def main():
    d = {}
    print available_commands()
    while True:
        user_input = raw_input('>>> ')
        check_command(user_input, d)


if __name__ == '__main__':
    main()
