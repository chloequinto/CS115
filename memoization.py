'''
Created on Feb 21, 2018

@author: Chloe Quinto
'''

'''
Memo-ization
0. Take the recursive function and make it a nested helper.
It will take an additional argument, the memo, which is initially an empty dictionary

1. Check if the key exists in the dictionary. If so, return the value of the associated with the key
2. Do the work! That is, use the recursion to compute the answer, and store it in a local variable

3. Store the result in the memo and return the result from the function 
'''
def fib (n):
    if n <= 1: 
        return n
    return fib(n-1) + fib (n-2)

#for i in range (50): 
#   print(i, fib(i))
    
def fib_memo(n):
    def fib_helper(n, memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            result = n
        else:
            result = fib_helper(n-1, memo) + fib_helper(n - 2, memo)
        memo[n] = result 
        return result 
    return fib_helper(n, {})

#for i in range (50): 
#    print(i, fib_memo(i))
    
    
def LCS(s1, s2):
    '''Returns the length of the longest common subsequence in strings s1 and s2 '''
    if s1 == '' or s2 == '':
        return 0 
    if s1[0] == s2[0]: 
        return 1 + LCS(s1[1:], s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))
    
#print(LCS('spots', 'pto'))

def LCS_memo(s1,s2):
    def LCS_helper(s1, s2, memo):
        if (s1, s2) in memo: 
            return memo[(s1,s2)]
        
        if s1 == '' or s2 == '': 
            result = 0
        elif s1[0] == s2[0]:
            result = 1 +LCS_helper(s1[1:], s2[1:], memo)
        else: 
            result = max(LCS_helper(s1, s2[1:],memo), LCS_helper(s1[1:], s2,memo))
        memo[s1,s2] = result
        return result
    return LCS_helper(s1,s2,{})

print(LCS_memo('chloe', 'chloeqqqqq'))

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
#print(LCS_with_values('spots', 'spto'))

def fast_LCS_with_values (s1, s2):
    def fast_LCS_helper(s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1,s2)]
        
        if s1 == '' or s2 == '':
            result = (0, '')
        elif s1[0] == s2[0]: 
            lose_both = fast_LCS_helper(s1[1:], s2[1:], memo)
            result = (1 + lose_both[0], s1[0] + lose_both[1])
        else: 
            uses1 = fast_LCS_helper(s1, s2[1:], memo)
            uses2 = fast_LCS_helper(s1[1:], s2, memo)
            if uses1[0] > uses2[0]: 
                result = uses1
            else: 
                result= uses2
        memo[(s1,s2)] = result
        return result
    return fast_LCS_helper(s1, s2, {})

print(fast_LCS_with_values('spots', 'spto'))