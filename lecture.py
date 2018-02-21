'''
Created on Feb 8, 2018

@author: Chloe Quinto
'''

"""
if s1 is '' or s2 '' -> 0 
if first char is s1 == first char in s2: 
    1 + LCS(s1[1:], s2[1:])
    try LCS (s1, s2[1:])
        LCS (s1[1:], s2)
        -> return max 

"""


def LCS(s1, s2):
    '''Returns the length of the longest common subsequence in strings s1 and s2 '''
    if s1 == '' or s2 == '':
        return 0 
    if s1[0] == s2[0]: 
        return 1 + LCS(s1[1:], s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))
    
print(LCS('spots', 'pto'))

def LCS_with_values(s1, s2):
    """
    Returns a tuple containing the length of the longest common subsequence 
    in index 0 and the string in common in index 1 
    """
    if s1 == '' or s2 == '':
        return (0, '')
    if s1[0] == s2[0]: 
        result = LCS_with_values(s1[1:], s2[1:])
        return (1 + result[0], s1[0] + result [1])
    uses1 = LCS_with_values(s1, s2[1:])
    uses2 = LCS_with_values(s1[1:], s2)
    if uses1[0] > uses2[0]: 
        return uses1
    else: 
        return uses2
print(LCS_with_values('spots', 'spto'))