'''
Created on Jan 30, 2018

@author: Chloe Quinto
'''
from cs115 import map, reduce, filter
import math 

def factorial(n):
    if n == 0: 
        return 1
    return n * factorial(n-1)

def tower(n):
    if n == 0:
        return 1
    return 2 ** tower(n-1)

def tower_reduce(n):
    """Computes 2^(2) with n twos, using reduce"""
    def power(x,y):
        return y ** x 
    return reduce(power, [2]*n)

def length(lst):
    """returns the length of the list"""
    if lst == []:
        return 0 
    return 1 + length(lst[1:])

def reverse(lst):
    """tales as input a list of elements and returns the list in reverse order"""
    if lst == []:
        return []
    return reverse(lst[1: ]) + [lst[0]]

def member (x,lst):
    """returns true if x is contained in the list and false otherwise"""
    #no pending operation 
    """m(2, [1,2])
        m(2, [2])
        true 
     """
    if lst == []:
        return False
    if lst == [0]:
        return True
    return member(x, lst[1:])


def my_map (f, lst):
    """returns a new list where the function f has been applied to every element in the original list """
    if lst == []:
        return []
    return [f(lst[0])] + my_map(f, lst[1:])
    
    
    
    
print(map(factorial, range(0,10)))
print(tower(2))
print(map(tower, range
          (1,4)))
print(length([1,2,3]))
print(tower_reduce(1))
print(reverse([1,2,3]))

def sqr(x):
    return x * x


print(my_map(sqr, [4,5,6]))


def my_reduce (f, lst): 
    """Return the list to a single value as dictated by the predicate f."""
    def my_reduce_helper(f,lst, accum):
        if lst == []: 
            return accum
        return my_reduce_helper(f, lst[1:], f(accum, lst[0]))
    
    if lst == []: 
        raise TypeError('my_reduce() of empty sequence with no initial value')
    return my_reduce_helper (f, lst[1:], lst[0])
"""
def end3(x):
    return x % 10 == 3 
eliminated by lambda 

"""
print(filter(lambda x: x % 10 == 3, [3, 33, 243, 24]))
print(my_map(lambda x:x *x, [1,2,3,4]))


def prime(n):
    """takes an integer n and tells whether or not it is prime"""
    possible_divisors = range(2, int(math.sqrt(n)) + 1)
    divisor = filter(lambda x: n % x == 0, possible_divisors)
    return len(divisor) == 0 


def primes(n):
    """Takes an integer n finds all primes less than or equal to some given n """
    def sieve(lst):
        if lst == []: 
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n + 1))

"""
Test of Primes
print(primes(25))
"""

def fib(n):
    if n <= 1 : 
        return n
    return fib(n-1) + fib(n-2)
"""
Test for fib
print(fib(6))
"""