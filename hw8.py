'''
Created on Mar 27, 2018

@author: Chloe Quinto

Pledge:   I pledge my honor that I have abided by the Stevens Honor System  - cquinto - 10416964
CS115 - Hw 8
'''
def TcToNum(num):
    '''Input of string of 8 bits representing an integer in 
    two's complement and returns the corresponding integer '''
    def TcToNumHelper(num):
        if num == "": 
            return 0 
        return TcToNumHelper(num[:-1]) * 2 + int(num[-1])
    return TcToNumHelper(num[1:]) if num[0] == "0" else TcToNumHelper(num[1:]) - 128


def NumToTc(n):
    '''
    Take as input an integer N, and returns a string representing the two's 
    complement representation of that integer 
    '''
    def numToBinary(n):
        if n == 0: 
            return ""
        return numToBinary(int(n/2)) + str(n%2)
    
    def filler(s):
        '''fills if binary string is not enough'''
        return "0" * (7-len(s)) + s
    
    if n>= 128 or n <-128: 
        return 'Error'
    if n>= 0: 
        return "0" + filler(numToBinary(n))
    else:
        return "1" + filler(numToBinary(n+128))