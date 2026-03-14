def fib_list(n, memo=None):

    if memo is None:
        memo = [None] * (n + 1)
    

    if n <= 1:
        return n
    
 
    if memo[n] is not None:
        return memo[n]
    

    memo[n] = fib_list(n - 1, memo) + fib_list(n - 2, memo)
    return memo[n]


print(fib_list(10))