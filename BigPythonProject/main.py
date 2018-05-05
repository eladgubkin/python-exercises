def available_commands():
    return """Available Commands:
    
[set hp/mana <amount>]
[get hp/mana]
[add hp/mana <amount>]
[sub hp/mana <amount>]
[write hp/mana <myfile.txt>]
[load hp/mana <myfile.txt>]
[quit]
"""


def set_function(user_input_list):
    if len(user_input_list) == 3:
        if user_input_list[1] == 'hp' and user_input_list[2].isdigit():
            global hp
            hp = int(user_input_list[2])

        elif user_input_list[1] == 'mana' and user_input_list[2].isdigit():
            global mana
            mana = int(user_input_list[2])

        else:
            print 'SyntaxError: invalid syntax'
    else:
        print 'SyntaxError: invalid syntax'


def get_function(user_input_list):
    try:
        if len(user_input_list) == 2:

            if user_input_list[1] == 'hp':
                print hp

            elif user_input_list[1] == 'mana':
                print mana

            else:
                print "NameError: name '{}' is not defined".format(user_input_list[1])
        else:
            print 'SyntaxError: invalid syntax'
    except NameError:
        print "NameError: name '{}' is not defined".format(user_input_list[1])


def add_function(user_input_list):
    try:
        if user_input_list[1] == 'hp' and user_input_list[2].isdigit():
            global hp
            hp += int(user_input_list[2])

        elif user_input_list[1] == 'mana' and user_input_list[2].isdigit():
            global mana
            mana += int(user_input_list[2])
    except IndexError:
        print 'SyntaxError: invalid syntax'


def sub_function(user_input_list):
    try:
        if user_input_list[1] == 'hp':
            global hp
            hp -= int(user_input_list[2])

        elif user_input_list[1] == 'mana':
            global mana
            mana -= int(user_input_list[2])
    except IndexError:
        print 'SyntaxError: invalid syntax'


def write_function(user_input_list):
    try:
        if user_input_list[1] == 'hp' and user_input_list[2][-4:] == '.txt':
            with open(user_input_list[2], 'w') as write_file:
                write_file.write(str(hp))

        elif user_input_list[1] == 'mana' and user_input_list[2][-4:] == '.txt':
            with open(user_input_list[2], 'w') as write_file:
                write_file.write(str(mana))

        else:
            print "Error: Can't find file name"
    except IndexError:
        print 'SyntaxError: invalid syntax'


def load_function(user_input_list):
    try:
        if user_input_list[1] == 'hp' and user_input_list[2][-3:] == 'txt':
            with open(user_input_list[2], 'r') as read_file:
                try:
                    global hp
                    hp = int(read_file.read())
                except ValueError:
                    print "ValueError: invalid literal"

        elif user_input_list[1] == 'mana' and user_input_list[2][-3:] == 'txt':
            with open(user_input_list[2], 'r') as read_file:
                try:
                    global mana
                    mana = int(read_file.read())
                except ValueError:
                    print "ValueError: invalid literal"

        else:
            print 'SyntaxError: invalid syntax'
    except IndexError:
        print 'SyntaxError: invalid syntax'


def check_command(user_input):
    user_input_list = user_input.split(' ')

    if user_input_list[0] == 'set':
        set_function(user_input_list)

    elif user_input_list[0] == 'get':
        get_function(user_input_list)

    elif user_input_list[0] == 'add':
        add_function(user_input_list)

    elif user_input_list[0] == 'sub':
        sub_function(user_input_list)

    elif user_input_list[0] == 'write':
        write_function(user_input_list)

    elif user_input_list[0] == 'load':
        load_function(user_input_list)

    elif user_input == 'quit':
        quit()

    else:
        print "NameError: name '{}' is not defined".format(user_input)


def main():
    print available_commands()
    while True:
        user_input = raw_input('>>> ')
        check_command(user_input)


if __name__ == '__main__':
    main()
