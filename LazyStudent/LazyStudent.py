import sys


def calculate(line):
    try:
        left_number_str, operation, right_number_str = line.split()

        left_number = int(left_number_str)
        right_number = int(right_number_str)
    except ValueError:
        return ''

    if operation == '+':
        result = left_number + right_number
    elif operation == '-':
        result = left_number - right_number
    elif operation == '*':
        result = left_number * right_number
    elif operation == '/':
        result = left_number / right_number

    return ' '.join([left_number_str, operation, right_number_str, '=', str(result)])


def main():
    try:
        _, source_file_path, solution_file_path = sys.argv
    except ValueError:
        print 'USAGE: LazyStudent.py <source-file-path> <solution-file-path>'
        return

    with open(source_file_path, 'r') as source_file:
        lines = source_file.read().split('\n')

    solutions = filter(lambda item: item != '',
                       map(calculate, lines))

    with open(solution_file_path, 'w') as solution_file:
        solution_file.write('\n'.join(solutions))

    print 'Done'


if __name__ == '__main__':
    main()
