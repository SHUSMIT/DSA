def finbonacci(n,dp_arr):
    if n==0 or n==1:
        return 1
    
    if dp_arr[n] != -1:
        return dp_arr[n]
    
    dp_arr[n] = finbonacci(n-1,dp_arr) + finbonacci(n-2,dp_arr)

    return dp_arr[n]


def table_optimise(n):
    prev = 1
    prev2 = 0
    
    for i in range(2,n+1):
        curr = prev + prev2
        prev = curr
        prev2 = prev  ## space optimised, but observation

    return prev
    


n = int(input())
arr = {i : -1 for i in range(n+1)}
print(finbonacci(n,arr))
print(table_optimise(n))
