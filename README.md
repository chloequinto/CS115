# CS115

**Introduction to Python**

Repository containing all my homeworks, labs, and notes. 

## Index:

HW 1 - create functions that calculate the factorial of a number, mean of a list, prime of a number <br />
HW 2 - Scrabble Game <br />
HW 3 - create a function that returns the coins necessary for a given value, another Scrabble Score function, two functions that slice <br />
HW 4 - Pascal's Triangle <br />
HW 5 - Turtle Graph, Lucas numbers function, List of coins function



Lab 1 - create functions: inverse, e, add, absolute difference, difference<br />
Lab 2 - create functions: dot product, takes a string and returns list of characters, removes input from an element, returns evens, returns the reverse of a list (even elements within an element)<br />
Lab 3 - create a function that determines whether it is possible to create the target sum using values in a list<br />
Lab 4 - create a function that returns the max vakue, and the list of items that make the value without exceeding the capacity of the knapsack<br />
Lab 5 - using memoization, create functions that returns the edit distance between two strings, create a function finds the edit distance from a dictionary and the user_input word, spell-checker function <br />
Lab 6 - create functions: decimal to binary, binary to decimal, counter for binary, decimal to ternary, ternary to decimal <br/>


## Operators 
'+' addition <br/> 
'-' subtraction <br/> 
'*' multiplication <br/> 
'/' division <br/> 
'//' true division <br/> 
'**' exponential <br/> 

## Lists 
[0,1,2,3,4] <br/>
The first element in a list is in index[0], second element in a list is in index[1] and so forth. <br/> 
Syntax: <br/>
[include, exclude, step] 

## Memoization
Memoization is an optimization technique used to speed up programs by storing results of expensive function calls <br/> 

The following are steps for Memoization
1. Take the recursive function and make it a nested helper. It will take an additional argument, the memo, which is initially an empty dictionary<br/> 

2. Check if the key exists in the dictionary. If so, return the value of the associated with the key <br />
3. Do the work! That is, use the recusion to compute teh answer, and store it in a local variable <br /> 
3. Store the result in the memo and return the result from the function <br/>
