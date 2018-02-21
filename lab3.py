'''
Created on Feb 7, 2018

@author: Chloe Quinto

I pledge my honor that I have abided by the Stevens Honor System - cquinto
10416964
'''




def change(amount, coins):
    """Determines whether or not it is possible to create the target sum using the
    values in the list, values in the list can be positive, negative, or 0"""
    if amount == 0: 
        return 0
    if coins == []:
        return float("inf")
    if amount < coins[0]: 
        return change(amount, coins[1:])
    use_it = change(amount - coins[0], coins) + 1
    lose_it = change(amount, coins[1:])
    return min(use_it, lose_it)  

'''print(change(48, [24]))
print(change(48, [1,5,10,25,50]))
'''