
def fib(n, lst):
    
    if lst[n] == -1:
        if n <= 1:
            lst[n] = n
        else:
            lst[n] = fib((n - 1), lst) + fib((n - 2), lst)
    
    return lst[n]




n = 7
lst = [-1 for x in range(n + 1)]
print(fib(n, lst))