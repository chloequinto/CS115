'''
Created on Feb 14th 2018
@author:   Chloe Quinto 10416964 
0ledge:    I pledge my honor that I have abided by the Stevens Honor System - cquinto 

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(values, listOfCoins ):
    '''returns the amount of coins needed to create the amount and a list of coins
    '''
    
    if values == 0: 
        return (values, [])
    if listOfCoins == []: 
        return (float("inf"), [] )
    if values < listOfCoins[0]: 
        return giveChange(values, listOfCoins[1:])
    use_it = giveChange(values - listOfCoins[0], listOfCoins)
    x = (use_it[0] + 1 , [listOfCoins[0]] + use_it[1])
    lose_it = giveChange(values, listOfCoins[1:])
    if x[0] < lose_it[0]: 
        return x
    return lose_it  
   
#print(giveChange(48, [24]))     
#print(giveChange(0, [1,2,3,4]))
#print(giveChange(4, []))

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []: 
        return []
    
    def letterScore(letter, scrabbleScore):
        '''input of a single letter and outputs the value'''
        if scrabbleScore == []: 
            return 0
        if letter == scrabbleScore[0][0]: 
            return scrabbleScore[0][1]
        return letterScore(letter, scrabbleScore[1:])
    
    def wordScore(S, scoreList):
        """inputs string and finds total score """
        if S == '':
            return 0 
        return letterScore(S[0],scoreList) + wordScore(S[1:], scoreList)
        
    return [dct[0] , wordScore(dct[0], scores)]  + wordsWithScore(dct[1:], scores)
print(wordsWithScore(Dictionary, scrabbleScores))
#print(wordsWithScore(['yes', 'hello'], scrabbleScores))
#print(wordsWithScore([], scrabbleScores))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    #print(L)
    if n == 0: 
        return [L[0]]
    if L == []: 
        return [] 
    return [L[0]] + take(n-1, L[1:])

#print(take(4, [2,3,8,10,5,6,7]))



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    #print(L)
    if n == 0: 
        return L
    if L == []: 
        return []
    return drop(n-1, L[1:]) 

#print(drop(4, [2,3,8,10,5,6,7]))




