#1
#my_list = [True, 80, 60.5, 'Hello', False]
#print my_list[::2]


#2
#print sum([10, 11, 12, 0.75])


#3
#def summer(x):
    #if isinstance(x[0], basestring):
        #result = ''
        #for i in x:
            #result = i + result
            #return result


#print summer([10, 11, 12, 0.75])
#print summer([True, False, True, True])
#print summer(['aa', 'bb', 'cc'])
#print summer([1, 2, 3, 'a'], [4, 'b', 'c', 'd'


#4
def last(my_str):
    return my_str[-1]


def main():
    benjamins = ['p.daddy', 'lil.kim', 'dr.dre', 'n.big']
    benjamins.sort(key=last)
    print(benjamins)


print(main())
