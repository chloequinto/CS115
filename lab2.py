'''
Created on Feb 1, 2018

@author: Chloe Quinto
I pledge my honor that I have abided by the Stevens Honor System 

'''

"""
Lab 1 requires 6 functions

1. dot(L, K) which should output the dot product of the lists L and K
"""


def dot(L, K):
    """ outputs the dot product of the lists L and K """
    if L == [] or K == []: 
        return 0
    
    return L[0]*K[0] + dot(L[1:], K[1:])

"""
Tests for Dot Functions 

print(dot([],[]))
print(dot([1] , [6]))
print(dot([5,3] , [6]))
"""

def explode(S):
    """ take a string s as input and should return a list of characteres"""
    if S == "": 
        return []
    return [S[0]] + explode(S[1:])

"""
Tests for explode functions 
print(explode("spam"))

"""

def ind(e,L):
    """Takes an element and a sequence L and returns the index at which e is first found in L """
    if L == []: 
        return 0 
    if L == '': 
        return 0
    elif e == L[0]:
        return 0 
    return 1 + ind(e, L[1:])




print(ind(1, [1,2,3,4]))

"""
Tests for ind functions

print(ind(42, ['hi', 42]))
"""


def removeAll(e, L):
    """takes in an element e and a list L. Then it should 
    return another list that is identical to L except that all elements identical to e 
    has been remove"""
    if L == []:
        return [] 
    if e == L[0]:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:]) 


"""
Tests for removeAll functions

print(removeAll(3, [1,2,3]))

"""

    

def myFilter(s, L):
    """Returns all evens from a list"""
    if L == []:
        return [] 
    if s(L[0]):
        return [L[0]] + myFilter(s, L[1:])
    return myFilter(s, L[1:]) 

"""
Tests for Filter

def even(n):
    return n % 2 == 0

print(myFilter(even, [0,1,2,3]))
"""

      
def deepReverse(L):
    """Takes a list of elements and returns the reverse even elements within an element  """
    if L == []: 
        return []
    if isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    return deepReverse(L[1:]) + [L[0]] 

"""
Tests for deepReverse
print(deepReverse([1,2, 5, 7, 8]))
"""

