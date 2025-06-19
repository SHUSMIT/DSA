def subset_sum_k(idx,target,arr):
    if target == 0:
        return True
    
    if idx == 0: ## start reached
        return arr[idx] == target
    
    not_take = subset_sum_k(idx-1,target,arr) ## no reduction
    
    take = False
    if arr[idx] <= target:
        take = subset_sum_k(idx-1,target-arr[idx],arr) ## target always >= 0 so check
    
    return take or not_take

def memoise(idx,target,arr,dp):
    if target == 0:
        return True
    
    if idx == 0: ## start reached
        return arr[idx] == target
    
    if dp[idx][target] != -1:
        return dp[idx][target]
    
    not_take = memoise(idx-1,target,arr,dp) ## no reduction
    
    take = False
    if arr[idx] <= target:
        take = memoise(idx-1,target-arr[idx],arr,dp) ## target always >= 0 so check
    
    dp[idx][target] = take or not_take
    
    return dp[idx][target]

def tabulation(arr):
    n = len(arr)
    dp = [[-1 for _ in range(target)] for _ in range(n)] ## idx,target = row,col
    
    for i in range(n):
        dp[i][0] = True ## target is 0
    
    for i in range(n):
        dp[i][arr[0]] = True ## target value quals arr[0]
        
    ## 0 done calculated
    for i in range(1,n):
        for j in range(1,target):
            
            not_take = dp[i-1][target] ## no reduction
    
            take = False
            if arr[idx] <= target:
                take = dp[idx-1][target-arr[i]] ## target always >= 0 so check
            
            dp[i][j] = take or not_take
            
    return dp[len(arr)-1][target]
            
    
    
    
    
    
    