def coins_deno(idx,arr,target): 
    
    if idx == 0:
        if target % arr[0] == 0: ## target is divisible by final index
            return target / arr[0]
        else:
            return 0
            
    if target == 0:
        return 1
    
    not_take = coins_deno(idx-1,arr,target) ## not take
    take = float('inf')
    if target >= arr[idx]:
        take = 1 + coins_deno(idx,arr,target-arr[idx]) ## take deno, always repeat, infinite possible
    
    return min(take,not_take)
    
    

def memoise(idx,arr,target,dp): 

    if idx == 0:
        if target % arr[0] == 0: ## target is divisible by final index
            return target / arr[0]
        else:
            return 0
    
    if dp[idx][target] != -1:
        return dp[idx][target]

    not_take = coins_deno(idx-1,arr,target) ## not take
    take = float('inf')
    if target >= arr[idx]:
        take = 1 + coins_deno(idx,arr,target-arr[idx]) ## take deno, always repeat, infinite possible
    
    dp[idx][target] = min(take,not_take)
    
    return dp[idx][target]


def tabular(arr,target): 
    ## 0 -- > n-1 move
    n = len(arr)
    
    dp = [[0 for _ in range(target+1)] for _ in range(n)] ## dp[idx][target]
    
    ## 0 to T
    for i in range(target+1): #i is target val 
        if i % a[0]:
            dp[0][i] = i % arr[0]
        else:
            dp[0][i] = float('inf')
    
    for i in range(1,n): ## go towards idx
        for j in range(target+1): ## go towards target
        
        not_take = dp[i-1][j] 
        take = float('inf')
        if j >= arr[i]:
            take = 1 + dp[i][j-arr[i]] ## take deno again -- always repeat, infinite possible we do this
        
        dp[i][j] = min(take,not_take)
    
    return dp[n-1][target]

def space_optimal(arr,target):
    n = len(arr)

    temp = [0 for _ in range(T+1)]

    for i in range(target+1): 
        if i % a[0]:
            temp[i] = i % arr[0]
        else:
            temp[i] = float('inf')
    
    for i in range(1,n): ## go towards idx
        curr = [0 for _ in range(T+1)]
        
        for j in range(T+1): ## go towards target
        
        not_take = temp[j] 
        take = float('inf')
        if j >= arr[i]:
            take = 1 + temp[j-arr[i]] ## take deno again -- always repeat, infinite possible we do this
        
        curr[j] = min(take,not_take)
        temp = curr
    
    return temp[target]