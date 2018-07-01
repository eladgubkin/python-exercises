# returns the average difference between 2 lists

list1 = [1, 2, 3, 4]
list2 = [1, 1, 1, 1]


def avg_diff(lst1, lst2):
    return sum([abs(i - j) for i, j in zip(lst1, lst2)]) / float(len(lst1))


print(avg_diff(list1, list2))
