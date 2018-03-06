'''
Created on March 6 2018
@author:  Chloe Quinto
Pledge:   I pledge my honor that I have abided by the Stevens Honor System  - cquinto - 10416964
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

#Max run length is 31
#numToBinary and binaryToNum taken from lab 6 

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    return numToBinary(int(n / 2)) + str(n%2)

def filler(s):
    '''complete 5 digit if the binary string is not long enough, fill higher digits with 0.'''
    return "0" * (5 - len(s)) + s

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1])

def compress(s):
    '''compress binary string and return compressed binary string'''
    def comp_helper(s, ex):
        '''return an array  ["0", 0], the first element shows whether it is a 1 or 
        0 and the second element shows how long the 1 or 0 is'''
        if s == "":
            return [ex]
        if s[0] != ex[0] and ex[1] != 0:
                return [ex] + comp_helper(s[1:], [s[0]] + [1])
        return comp_helper(s[1:], [s[0]] + [ex[1] + 1])

    def compress_more(lst):
        '''takes the result from comp_helper(), returns binary string of base 10. Split if consecutive 1 or 0 is larger than MAX_RUN_LENGTH'''
        if lst == []:
            return ""
        if lst[0][1] > MAX_RUN_LENGTH:
            return "1111100000" + compress_more([[lst[0][0]] + [lst[0][1]-31]] + lst[1:])
        return filler(numToBinary(lst[0][1])) + compress_more(lst[1:])

    return ("00000" if s[0] == "1" else "") + compress_more(comp_helper(s, ["0",0]))



def uncompress(s):
    '''returns the uncompressed binary '''
    def uncompress_more(s):
        '''uncompress binary and return a list of numbers of consecutive 0 and 1'''
        if s == "":
            return []
        return [binaryToNum(s[0:COMPRESSED_BLOCK_SIZE])] + uncompress_more(s[COMPRESSED_BLOCK_SIZE:]) # first arg +1

    def uncomp_helper(lst, zero):
        '''takes result from uncompress_more() and gives the original binary string '''
        if lst == []:
            return ""
        return ("0" if zero else "1" ) * lst[0] + uncomp_helper(lst[1:], not zero)

    return uncomp_helper(uncompress_more(s), True)


def compression(s):
    '''returns the ratio of the compressed size to the original size for image S'''
    return len(compress(s)) / len(s)


##############Test Cases########################################
'''0*64
Since this compression is longer than MAX LENGTH, result should be split '''
#print(compress("0" * 64))
##############################################################
''''11 *32 '''
#print(compress("11" * 64))
#print(uncompress("11" * 64 ))
#print(compression("11"*64))
#############################################################
#print(compression('1' * (MAX_RUN_LENGTH + 1) + '1' * (MAX_RUN_LENGTH + 1) + '1' * (64 - 2 * MAX_RUN_LENGTH - 2)))
#############################################################
'''Penguin '''
#print(compress("00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"))
'''Smile '''
#print(compression("0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8))
'''Five'''
#print(compression("1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"))