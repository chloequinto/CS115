def fibonacci(n):
    '''returns fib number''' 
    if n <= 1: 
        return n 
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(20))

def fib_memo(n):
    '''Returns fib number using dictionary'''
    def fib_helper(n, memo):
        if n in memo: 
            return memo[n]
        if n <= 1: 
            result = n 
        else: 
            result = fib_helper(n-1, memo) + fib_helper(n-2, memo)
        memo[n] = result
        return result
    return fib_helper(n, {})


def tribonacci(n):
    '''
      Returns the nth tribonacci number. The 0th number is 0, the 1st number is 0, the second number is 1 and any number beyond
      is the sum of the previous three
  
      Example: 
      tribonacci(0) -> 0 
      tribonnaci(2) -> 1
      tribonacci(5) -> 4
      '''
    if n<=1: 
        return 0 
    if n == 2: 
        return 1 
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
  
#print(tribonacci(5))


def trib_memo(n):
    ''' 
    Returns the nth tribonacci number using memoization
    '''
    def trib_helper(n, memo):
        if n in memo: 
            return memo[n]
        if n <= 1: 
            result = 0
        elif n == 2: 
            result = 1 
        else: 
            result = trib_helper(n-1, memo) + trib_helper(n-2, memo) + trib_helper(n-3, memo)
        memo[n] = result
        return result
    return trib_helper(n, {})

#print(trib_memo(5))
