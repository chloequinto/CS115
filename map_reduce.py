'''
Created on Jan 25, 2018

@author: Chloe Quinto
'''

'''
Range 
range(stop) -> [ 0, 1, 2,...stop-1]
                [0, stop)

range(3)-> [0,1,2]

range(start, stop) -> [start, start+1, ... stop-1] 
range(2,5) -> [2,3,4] 

range(start, stop, step) -> [start, stop) going up or down step units between element s
range(2,10) -> [2,4,6,8]
range (2,9,2) -> [2,4,6,8]
range (10,0,-2) -> [10,8,6,4,2] 



'''
from cs115 import reduce

def span(lst):
    """returns the difference between the maximum and minimum number in a list""" 
    return reduce(max,lst)-reduce(min,lst) 

def gauss (n):
    """takes as input a positive integer n and returns the sum 1 + 2 + 3+...n"""
    return reduce(add(1,n+1))

def add(a,b):
    """returns the sum of a and b"""
    return a +b

def sum_of_squares(n):
    """takes an input a positive integer n and returns the sum 
    1^2+2^2+3^2+4^...."""
    return reduce(add , map(exp, range(1, n+1)))
     
def exp(a):
    """Returns the square of a """
    return a*a

print(span([3,4,42,7,-1]))
