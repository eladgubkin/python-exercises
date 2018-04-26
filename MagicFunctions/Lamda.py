# sorting the list by its absolute number

my_list = [2, -8, 5, -6, -1, 3]

my_list.sort(key=lambda number: abs(number))

print my_list
