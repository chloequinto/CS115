'''
Created on Jan 28, 2018

@author: Chloe Quinto

I pledge my honor that I have abided by the Stevens Honor System 

'''
"""
HW 1 is asking us to create three functions 

def factorial(n) which takes a positive integer n and returns n!

def mean (L) which takes a list as input and returns the mean (average) value 
of that list
 
 def prime(n) takes a positive integer n as input and returns True or False
 depending on whether n is prime or composite 

"""
from cs115 import reduce, map


def mult (x, y):
    """Returns the product of x and y"""
    return x * y

def factorial(n):
    """takes a positive integer n and returns n!"""
    return reduce(mult, range(1, n+1))

def mean(b):
    """takes a list as an input and returns the average value"""
    return reduce(add, b)/ len(b)

def add(a, b):
    """adds to inputs together"""
    return a + b

def divides(n):
    """takes an input n and another input K to see if there is a remainder when they're divided"""
    def div(k):
        return n % k == 0
    return div

    
def prime(n):
    """takes a positive integer as input and returns True or False depending on whether it is prime"""
    if n <= 2 or reduce(add, map(divides(n), (range(2,n)))) == 0:
        return True;  
    return False
    
"""



#Tests 

"""
print(factorial(7))
print(mean([1,2,3,4,5,6]))
print(prime(4))


