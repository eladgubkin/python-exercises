import shutil

old_file = r'E:\code\Python 2\SomeText.txt'
new_file = r'E:\code\Python 2\EmptyText.txt'


def read_file():
    with open(old_file, 'r') as input_file:
        print('The text in this file is:\n')
        for line in input_file:
            print(line,)
        copy_file()


def copy_file():
    shutil.copy(old_file, new_file)
    print('\n\n*File copy done*\n')
    delete()


def questions():
    question = input('Do you want to read and copy from old_file to new_file? [Yes] [No]\n')
    if question.lower() == 'yes':
        read_file()
    else:
        print('Okay....')


def delete():
    question_2 = input('Do you want to delete new_file? [Yes] [No]\n')
    if question_2.lower() == 'yes':
        with open(new_file, "w"):
            pass
    else:
        print('oh okay...')


questions()