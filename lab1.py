'''
Created on Jan 25, 2018

@author: Chloe Quinto

I pledge my honor that I have abided by the Stevens honor system 
'''

from cs115 import reduce, map
import math

def inverse(n):
    """takes a number n as input and returns the reciprocal"""
    return 1/n


def e(c):
    """returns approximate value of e in Taylor Expansion"""
    return reduce(add, map (inverse, map(math.factorial, range(0,c+1))))
   

def add(a,b):
    """Adds a and b together"""
    return a + b 

def error(r):
    """returns the absolute value of the diff between 
    actual value of e and the approximation of e(r)"""
    return abs(difference(math.e, e(r)))

def difference(y,z):
    """returns difference"""
    return y - z
    


