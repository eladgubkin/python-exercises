# both functions are doing the same thing-
# returns the given string without ['b', 'B']


def anti_bb(string):
    new_string = []
    for letter in string:
        if letter not in ['B', 'b']:
            new_string.append(letter)

    return ''.join(new_string)


def anti_b(string):
    new_string = [letter for letter in string if letter not in ['B', 'b']]

    return ''.join(new_string)


print(anti_bb('BBbbBbHelloBBBBbbbb'))

print(anti_b('BBbbHolaBBbb'))
