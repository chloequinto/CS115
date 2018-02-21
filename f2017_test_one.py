'''
Created on Feb 14, 2018

@author: Chloe Quinto
'''

from cs115 import map, filter
L = ['jack', 'and', 'jill', 'went', 'up', 'the', 'hill' ]
M = range(2, len(L), 2)
#print(M[1])

############################
def collapse(lst):
    #print(lst)
    if lst == []: 
        return []
    if isinstance(lst[0], list):
        print(lst)
        return collapse(lst[0]) + collapse(lst[1:])
    return [lst[0]] + collapse(lst[1:])


#print(collapse([1, [2,3]]))


def keep_large_squares(lst, threshold):
    return filter(lambda x: x > threshold, map(lambda x: x**2, lst))


print(keep_large_squares([-10, 2,3,20], 50))