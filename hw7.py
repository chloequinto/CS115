'''
Created on Mar 20, 2018

@author: Chloe Quinto
Pledge: "I pledge my honor that I have abided by the Stevens Honor System - cquinto
10416964

'''
# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = { 
('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }



def numToBaseB(N,B):
    '''Takes as input a non-negative integer N and a base B
    and returns a string representing the number N in base B  '''
    if N == 0: 
        return "0"
    return str(int(numToBaseB(int (N/B), B) + str(N % B)))

# print(numToBaseB(4,2))
# print(numToBaseB(4,3))
# print(numToBaseB(4,4))
# print(numToBaseB(0,4))
# print(numToBaseB(0,2))

def baseBToNum (S,B):
    '''takes as input a string S and a base B where S represents a number in 
    base B where B is between 2 and 10 inclusive '''
    if S == "":
        return 0 
    return baseBToNum(S[:-1],B) * B + int(S[-1])

# print(baseBToNum("11",2))
# print(baseBToNum("11",3))
# print(baseBToNum("11",10))
# print(baseBToNum("",10))

def baseToBase(B1,B2,SinB1):
    '''Takes inputs, B1 = base and B2 = base and SinB = string representing
    a number in base B1. It should return a string representing the same number
    in base B2 '''
    return numToBaseB(baseBToNum(SinB1,B1), B2)

# print(baseToBase(2,10,"11"))
# print(baseToBase(10,2,"3"))
# print(baseToBase(3,5,"11"))

def add(S,T):
    '''takes two binary strings and returns their sum in binary '''
    return numToBaseB(baseBToNum(S,2) + baseBToNum(T,2), 2)

# print(add("11", "01"))
# print(add("011", "100" ))
# print(add("110", "011"))


def addB(S,T):
    '''returns a new string representing the sum of two input strings '''
    diff= len(S) - len(T)
    if diff > 0:
        T = "0" * diff + T
    if diff < 0:
        S = "0" + diff + S 
    
    def addBHelper(C,S,T):
        if S == "": 
            return "" if C == "0" else "1"
        return addBHelper(FullAdder[(C, S[-1], T[-1])][1], S[:-1], T[:-1]) + FullAdder[(C, S[-1], T[-1])][0]
    return addBHelper ("0", S, T)


# print(addB("11", "1"))
# print(addB("011", "100"))