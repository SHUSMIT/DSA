def mcm(i,j,arr): ## steps to multiply mat i to mat j, initially 1 and n-1 ( not 0)
    if i == j:
        return 0
    
    mini= float('inf')

    for k in range(i,j):  ## go from i to j-1 --> partition of (i,k) (k+1,j)

        steps = arr[i-1] * arr[k] * arr[j] + mcm(i,k,arr) + mcm(k+1,j,arr)
        mini = min(mini,steps)
    
    return mini

def memoise(i,j,arr,dp):

    if i == j:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]

    mini= float('inf')

    for k in range(i,j):  ## go from i to j-1 --> partition of (i,k) (k+1,j)

        steps = arr[i-1] * arr[k] * arr[j] + mcm(i,k,arr,dp) + mcm(k+1,j,arr,dp)
        mini = min(mini,steps)
    
    dp[i][j] = mini

    return dp[i][j]

def tabular(arr):
    n = len(arr)
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    ## now reverse i --> (n-1) to 0 and j from i to n-1 (not 0 as i always left of j)

    for i in range(n-1,0,-1): # i upto 1
        for j in range(i+1,n):

            for k in range(i,j):  ## go from i to j-1 --> partition of (i,k) (k+1,j)

                steps = arr[i-1] * arr[k] * arr[j] + dp[i][k]+ dp[k+1][j]

                dp[i][j] = min(dp[i][j],steps)
    
    return dp[1][n-1]