'''
Created on Feb 20, 2018

@author: Chloe Quinto
I pledge my honor that I have abided by the Stevens Honor System - Chloe Quinto, cquinto, 10416964
'''

def pascal_row(n):
    '''takes a single integer n and outputs the corresponding pascal's row'''
    def add (row):
        '''adds previous rows'''
        if len(row) <= 1: 
            return []
        return [row[0] + row[1]] + add(row[1:])
    def helper(n, row):
        '''adds [1] + the previous row's addition + [1] '''
        if n == 0: 
            return row 
        return helper(n-1, [1] + add(row) + [1])
    return helper(n, [1])

#print(pascal_row(0))
#print(pascal_row(1))
#print(pascal_row(5))

def pascal_triangle(n):
    '''takes an input n and returns a list of lists containing the values of all the rows up to
    and including row n '''
    if n < 0: 
        return []
    return pascal_triangle(n-1) + [pascal_row(n)]

#print(pascal_triangle(0))
#print(pascal_triangle(1))
#print(pascal_triangle(5))