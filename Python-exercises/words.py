def both_ends(s):
    if len(s) <= 2:
        print('-')

    elif len(s) == 3:
        print(s[0] + s[1] + s[2])

    else:
         print(s[0] + s[1] + s[-2] + s[-1])


both_ends(input('Please enter a string'))
