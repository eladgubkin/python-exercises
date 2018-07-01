# This should be done using map()

# Returns the given string with each letter being multiplied
# Cyber -> CCyybbeerr


# without list comprehensions:

def letter_double(string):
    result = ''
    for letter in string:
        result += letter + letter
    return result


print(letter_double('Cyber'))


# with list comprehensions:

def double(string):
    dbl = [letter + letter for letter in string]
    return ''.join(dbl)


print(double('Cyber'))


# with map() function:

n = ['Cyber', 'Hello', 'Sup']
print(list(map(lambda x: (letter + letter for letter in x), n)))
