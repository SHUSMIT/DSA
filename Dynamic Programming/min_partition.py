def tabular(arr,target):
    dp = [[-1 for _ in range(target) ] for _ in range(len(arr))]
    
    for i in range(len(arr)):
        dp[i][0] = True
    for i in range(len(arr)):
        dp[0][i] = True
        
    ## now go 1 to n-1 for each 
    for i in range(1,len(arr)):
        for j in range(1,len(arr)):
            
                not_take = dp[i][j]
                take = False
                if target >= arr[i]:
                    take = dp[i][j]
                
                dp[i][j] = take or not_take
    
    return dp[len(arr)-1]  ## return me the last row that contains all target values possible or not

def min_partition(arr):
    
    S = sum(arr)
   
    arr = tabular(arr,S)
    n = len(arr)
    mini = float('inf')
    
    for i in range(n//2):
        if arr[i]:
            s1 = i
            s2 = S - i
            mini = min(mini, abs(s1-s2))
    
    return mini