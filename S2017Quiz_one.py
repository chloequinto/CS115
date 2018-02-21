'''
Created on Feb 13, 2018

@author: Chloe Quinto
'''
def collapse(lst):
    
    if lst == []: 
        return []
    if isinstance(lst[0], list): 
        
        """print(lst)""" 
        return collapse(lst[0]) + collapse(lst[1:])
    return [lst[0]] + collapse(lst[1:])

#print(collapse([1, [2,3], [[4,5], [6]], 7 ]))

L = ['the', 'innovation', 'university', 'Stevens', 'is']
M = range (2, 4)
print(L[1:4:2])
