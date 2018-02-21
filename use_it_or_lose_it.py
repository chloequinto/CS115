'''
Created on Feb 5, 2018

@author: Chloe Quinto

'''

from cs115 import map

def powerset(lst):
    """Returns the power set of the list, that is the set of all subsets """
    if lst == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]] + subset , lose_it)
    return lose_it + use_it


print(powerset([1,2,3]))


"""Given a target sum 7, is it possible to build it from this list of values [5,1,2] """

def subset(target, lst):
    """Determines whether or not it is possible to create the target sum using the
    values in the list, values in the list can be positive, negative, or 0"""
    if target == 0: 
        return True 
    if lst == []: 
        return False
    use_it = subset(target - lst[0], lst[1:])
    lose_it = subset(target, lst[1:])
    return use_it or lose_it 

print(subset(7, [5,1,2])) 

"""
And and or are short circuit operators, if the result can be deduced by evaluating only the first operand .there is no need to ever evaluate the second operand 
"""

def better_subset(target, lst):
    if target == 0: 
        return True 
    if lst == []: 
        return False
    return better_subset(target - lst[0], lst[1:]) or better_subset(target, lst[1:])

print(better_subset(7, [5,1,2]))


def subset_with_values(target, lst):
    """Determines whether or not it is possible to create the target sum using the
    values in the list, values in the list can be positive, negative, or 0. The function returns a tuple of values 
    of exactly two items, the first term is a Boolean that indicates True if the sum is possible  and false if it is not. 
    The second element in the tuple is a list of all the values that add up to male a target sum"""
    if target == 0: 
        return (True, [])
    if lst == []: 
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0]:
        return (True,[lst[0]] + use_it[1])
    return subset_with_values(target, lst[1:])

print(subset_with_values(7, [5,1,2]))


def distance (first, second):
    ''' Returns the edit distance between first and second strings''' 
    if first == '': 
        return len(second)
    if second == '': 
        return len(first)
    if second[0] == first[0]: 
        return distance (first[1:], second[1:])
    substitution =  distance(first[1:], second[1:])
    deletion =  distance(first[1:], second)
    insertion =  distance(first, second[1:])
    return 1 + min(substitution, deletion, insertion )

print(distance('cat', 'ba') )
print(distance('zoom', 'moon'))


def coin_row(n):
    if n == []:
        return 0 
    return max(n[0] +coin_row(n[2:]), coin_row(n[1:]))

print(coin_row([5,1,2,10,6,2]))


def coin_row_with_values(lst):
    if lst == []: 
        return (0, [])
    use_it = coin_row_with_values(lst[2:])
    new_sum = use_it[0] + lst[0]
    lose_it = coin_row_with_values(lst[1:])
    if new_sum > lose_it[0]: 
        return (new_sum, [lst[0]] + use_it[1]) 
    return lose_it 

print(coin_row_with_values([5,1,2,10,6,2]))