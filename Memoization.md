Memoization is an optimization technique used to speed up programs by storing results of expensive function calls <br/> 

The following are steps for Memoization
1. Take the recursive function and make it a nested helper. It will take an additional argument, the memo, which is initially an empty dictionary<br/> 

2. Check if the key exists in the dictionary. If so, return the value of the associated with the key <br />
3. Do the work! That is, use the recusion to compute teh answer, and store it in a local variable <br /> 
3. Store the result in the memo and return the result from the function <br/>
