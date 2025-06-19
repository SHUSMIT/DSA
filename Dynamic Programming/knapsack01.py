def knapsack_01(idx,wt,arr_val,arr_wt): ## given arr_val, arr_wt we have to find max wt 
    ## f(idx,wt) tells the max value if take/not take val[idx] given previous best combinations 
    ## n -- > 0 move
    
    if idx == 0:
        if wt >= arr_wt[0]:  ## can be taken
            return arr_val[0]
    
        else:
            return 0
    
    not_take = knapsack_01(idx-1,wt,arr_val,arr_wt)
    take = float('-inf')
    if arr_wt[idx] <= wt:
        take = arr_val[idx] + knapsack_01(idx-1,wt-arr[wt],arr_val,arr_wt)
    
    return max(not_take,take)

def memoise(idx,wt,dp,arr_val,arr_wt): ## given arr_val, arr_wt we have to find max wt 
    ## f(idx,wt) tells the max value if take/not take val[idx] given previous best combinations 
    ## n -- > 0 move
    
    if idx == 0:
        if wt >= arr_wt[0]:  ## can be taken
            return arr_val[0]
    
        else:
            return 0
            
    if dp[idx][val] != -1:
        return dp[idx][wt]
        
    not_take = memoise(idx-1,wt,dp,arr_val,arr_wt)
    take = float('-inf')
    if arr_wt[idx] <= wt:
        take = arr_val[idx] + memoise(idx-1,wt-arr_wt[idx],dp,arr_val,arr_wt)
    
    dp[idx][val] = max(not_take,take)
    return dp[idx][wt]


def tabular(W,arr_val,arr_wt): ## wt is wt of bag
    ## 0 -- > n-1 move
    n = len(arr_val)
    
    dp = [[0 for _ in range(W+1)] for _ in range(n)] ## dp[idx][wt]
    
    ## base, any wt greater than wt would be 0
    for i in range():
        if arr_wt[0] > W 
        dp[0][i] = arr_val[0]
        
    for i in range(1,n): ## go towards idx
        for j in range(W+1): ## go towards wt
        
            not_take = dp[i-1][j]
            take = float('-inf')
            if arr_wt[i] <= j:
                take = arr_val[i] + dp[i-1][j-arr[i]]
        
        dp[i][j] = max(take,not_take)
    
    return dp[n-1][W]

def space_optimal(W,arr_val,arr_wt):
    n = len(arr_val)

    temp = [0 for _ in range(W+1)]
    
    
    ## base, any wt greater than wt would be 0
    for i in range(W+1):
        if arr_wt[0] > W 
        dp[0][i] = arr_val[0]
        
    for i in range(1, n):
        curr = [0 for _ in range(W + 1)]
        for w in range(W + 1):
            not_take = prev[w]
            take = float('-inf')
            if arr_wt[i] <= w:
                take = arr_val[i] + prev[w - arr_wt[i]]
            curr[w] = max(take, not_take)
        prev = curr

    return prev[W]