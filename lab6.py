'''
Created on March 1st 2018
@author:   Chloe Quinto
Pledge:   I pledge my honor that I have abided by the Stevens Honor System - cquinto 10416964

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0: 
        return False
    return True

#print(isOdd(4))
#print(isOdd(3))

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0: 
        return ''
    elif isOdd(n): 
        '''Needs to return integer  '''
        return numToBinary(int(n /2)) + '1'
    else: 
        return numToBinary(int(n/2)) + '0'


#print(numToBinary(0))
#print(numToBinary(1))
#print(numToBinary(4))
#print(numToBinary(10))
#print(numToBinary(36))

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        return binaryToNum(s[:-1]) * 2  + int(s[-1]) 

#print(binaryToNum(""))
#print(binaryToNum("0"))
#print(binaryToNum("1011"))
#print(binaryToNum("111"))
def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return ('0' * 8 + numToBinary(binaryToNum(s) + 1))[-8:]

# print(increment('00000000'))
# print(increment('00000001'))
# print(increment('00000111'))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n > 0:
        print(s)
        return count(increment(s), n-1)
    print(s)

#print(count("00000000", 4))

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    ''' 
    1120
    We want: 0 *1 + 2*3 + 1*9+ 1*27 == 42  
    '''
    if n == 0: 
        return ''
    s = n % 3 
    return numToTernary(int(n/3)) + str(s)
    

#print(numToTernary(42))

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '': 
        return 0
    return ternaryToNum(s[:-1]) * 3 + int(s[-1])

#print(ternaryToNum("1120"))
