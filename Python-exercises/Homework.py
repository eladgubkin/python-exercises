filename = 'Homework.txt'
solution_file = 'Solution.txt'


def reading_file():
        try:
            if x[1] == '+':
                return x[0], x[1], x[2], '=', int(x[0]) + int(x[2])
            elif x[1] == '-':
                return x[0], x[1], x[2], '=', int(x[0]) - int(x[2])
            elif x[1] == '*':
                return x[0], x[1], x[2], '=', int(x[0]) * int(x[2])
            elif x[1] == '/':
                return x[0], x[1], x[2], '=', int(x[0]) / int(x[2])
        except:
            return ''


def delete_content(s):
    with open(s, "w"):
        pass


def main(y, l):
    if l == 0:
        delete_content(solution_file)
    fdl = open(solution_file, 'a')
    fdl.writelines(str(y))
    fdl.close()


with open(filename, 'r') as our_file:
    l = 0
    for line in our_file:
        x = line.split()
        y = reading_file()
        main(" ".join(map(str, y)) + '\n', l)
        l = l + 1
