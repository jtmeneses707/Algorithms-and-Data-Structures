def fib_recur(n): # Recursive version of the fibonacci sequence
    if (n == 0):  # Has running time complexity of O(n!) as it must calculate each fib sequence before it again
        return 0
    elif (n== 1):
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n - 2) 