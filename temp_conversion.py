'''
Created on Jan 23, 2018

@author: Chloe Quinto
'''

'''
Data Types: 

string - sequence of characters 'hello' "bye" '123'
float - decimal number 3.14 - 2.3 
int - integers -2 0 23 
boolean - True/False 

Assignment 
a = 5 
a = (5 +3) /4

Mathematical Operators 
+
-
*
/ - true division 
% - modulus (remainder)
** - exponentiation  
 
5 % 2 = 1
2 % 5 = 2  

5/2 = 2.5 (always get a float) 
5.0/2 = 2.5 

5//2 = 2 
5.0//2 = 2.0 

Function
def double (x): 
    return 2*x
'''

def fahrenheit (celsius):
    """Returns the input celsius in fahrenheit"""
    return 9 / 5 * celsius + 32

def celsius (fahrenheit):
    """Returns the input fahrenheit to celsius"""
    return 5 / 9 * fahrenheit - 32  

"""
Call the functions below the definitions
"""

c = float (input('Enter degrees in Celsius: '))
f = fahrenheit(c) 

# You can print multiple items in each statement if you put commas 
""" input is a function that prompts the user for data"""
""" input is always a string"""

print(c, 'C = ', f , 'F')
print('%.2f C = %.2f F' %(c,f))

"""
Place Holders 
%d - int
%f - float 
%.2f - gives exactly 2 decimal places 
%s - string
"""


f = float (input('Enter degrees in Fahrenheit: '))
c = celsius(f)



print(f , 'F = ', c, 'C ')
print('%.2f F = %.2f C' %(f,c))

""" Try composition of functions 
Converting a Fahrenheit temperature to Celsius and back to Fahrenheit should 
give you the original Farenheit temperature 
"""

print () 
f = float (input ('Enter degrees in Fahrenheit: '))
"""Use assert to check the return value is equal to the expected value """
#assert fahrenheit(celsius) == f 
assert fahrenheit (celsius) == -1 # will produce an outcome incorrectly 
"""no output should be produced unless the assertion fails which means 
you have an error in your code or in your expectation 
"""















