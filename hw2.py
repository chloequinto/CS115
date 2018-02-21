'''
Created on _______________________
@author:  Chloe Quinto 
Pledge:    I pledge my honor that I have abided by the Stevens Honor System
cquinto/10416964

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

def letterScore(letter, scrabbleScores):
    """Takes as input a single letter and outputs the value """
    if scoreList == []: 
        return 0
    if letter == '':
        return 0
    if letter == scrabbleScores[0][0]:
        return scrabbleScores[0][1]
    return letterScore(letter,scrabbleScores[1:]) 


def wordScore(S, scoreList):
    """inputs string and finds total score """
    if S == '':
        return 0 
    return letterScore(S[0],scoreList) + wordScore(S[1:], scoreList)

def remove(i, L):
    '''removes a letter from a list and gives back the rest of the list'''
    if (i in L) == False: #if it is not in the list keep list 
        return L
    return L[0: L.index(i)] +L[L.index(i)+1:]

def possibleWord(S, Rack):
    '''checks a word from dictionary letter by letter if it is found in the rack, if so 
    you keep the letter, if not return False. Also removes repeated letters'''
    if S == '': 
        return True
    elif S[0] in Rack: 
        return possibleWord(S[1:], remove(S[0], Rack))
    return False 

def allowableWords(Rack):
    '''takes Dictionary as a parameter of possibleWord and filters words that can be made from Rack and puts it into a list '''
    return filter(lambda x: possibleWord(x, Rack), Dictionary )

def scoreWords(possibleWords):
    '''gives the total score for a possible word'''
    if possibleWords == []: 
        return []
    return [[possibleWords[0]] + [wordScore(possibleWords[0], scrabbleScores)]] + scoreWords(possibleWords[1:])

def scoreList(Rack):
    '''Returns possible words and its corresponding score given an rack'''
    return scoreWords(allowableWords(Rack))


def bestWord(Rack):
    '''Takes the score of a rack and checks it if it the maximum if so it outputs that maximum score and play  '''
    if scoreList(Rack) == []: 
        return ['', 0]
    maxScore = reduce(max, map(lambda x: x[1], scoreList(Rack)))
    bestPlays = filter(lambda x : x[1] == maxScore, scoreList(Rack))
    return bestPlays[0]
