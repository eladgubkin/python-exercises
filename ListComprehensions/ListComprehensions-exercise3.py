
# without list comprehensions:


my_list = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        my_list.append(i)

print(my_list)


# with list comprehensions:


i = [i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]

print(i)
