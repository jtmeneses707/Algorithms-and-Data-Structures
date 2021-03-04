def fib_recur(n): # Recursive version of the fibonacci sequence
    if (n == 0):  # Has running time complexity of O(n!) as it must calculate each fib sequence before it again
        return 0
    elif (n== 1):
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n - 2) 

def fib_dynamic(n): # DP version, using bottom up calculations with memoization
    table = [0, 1]  # T(n) = O(n), only has to run up to n - 1 times to calculate the nth fib number.
    i = 2
    for i in range(2, n+1):
        table.append(table[i-1] + table[i-2])

    return table[n]