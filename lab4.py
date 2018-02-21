'''
Created on Feb 15, 2018

@author: Chloe Quinto

I pledge my honor that I have abided by the Stevens Honor System - Chloe Quinto 
cquinto 
10416964 
'''

def knapsack(capacity, itemList):
    ''' Returns both the maximum value and the list of items that make this value without 
    exceeding the capacity of your knapsack'''
    if itemList == [] or capacity == 0: 
        return [0, []]
    lose_it = knapsack(capacity,itemList[1:])
    if capacity < itemList[0][0]:
        return lose_it
    use_it = knapsack(capacity - itemList[0][0], itemList[1:] ) 
    x = [use_it[0] + itemList[0][1], [itemList[0]] + use_it[1]]
    if x[0] > lose_it[0]: 
        return x 
    return lose_it
    
#print(knapsack(6, [[1, 4], [5, 10], [4, 180]]))
#print(knapsack(76, [ [36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))