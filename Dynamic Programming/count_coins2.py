def coins_deno2(idx,arr,target): 
    
    if idx == 0:
        if target % arr[0] == 0: ## target is divisible by final index
            return 1
        else:
            return 0
            
    if target == 0:
        return 1
    
    not_take = coins_deno2(idx-1,arr,target) ## not take
    take = 0
    if target >= arr[idx]:
        take = coins_deno2(idx,arr,target-arr[idx]) ## take deno, always repeat, infinite possible
    
    return take+not_take
    
    

def memoise(idx,arr,target,dp): 

    if idx == 0:
        if target % arr[0] == 0: ## target is divisible by final index
            return 1
        else:
            return 0
    
    if dp[idx][target] != -1:
        return dp[idx][target]

    not_take = memoise(idx-1,arr,target) ## not take
    take = 0
    if target >= arr[idx]:
        take = memoise(idx,arr,target-arr[idx]) ## take deno, always repeat, infinite possible
    
    dp[idx][target] = take+not_take
    
    return dp[idx][target]


def tabular(arr,target): 
    ## 0 -- > n-1 move
    n = len(arr)
    
    dp = [[0 for _ in range(target+1)] for _ in range(n)] ## dp[idx][target]
    
    ## 0 to T
    for i in range(target+1): #i is target val 
        if i % arr[0] == 0:
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    
    for i in range(1,n): ## go towards idx
        for j in range(target+1): ## go towards target
        
            not_take = dp[i-1][j] 
            take = 0
            if j >= arr[i]:
                take = dp[i][j-arr[i]] ## take deno again -- always repeat, infinite possible we do this
            
            dp[i][j] = take+not_take
    
    return dp[n-1][target]

def space_optimal(arr,target):
    n = len(arr)

    temp = [0 for _ in range(target+1)]

    for i in range(target+1): 
        if i % arr[0] == 0:
            temp[i] = 1
        else:
            temp[i] = 0
    
    for i in range(1,n): ## go towards idx
        curr = [0 for _ in range(target+1)]
        
        for j in range(target+1): ## go towards target
        
            not_take = temp[j] 
            take = 0
            if j >= arr[i]:
                take = temp[j-arr[i]] ## take deno again -- always repeat, infinite possible we do this
            curr[j] = take+not_take
            
        temp = curr
    
    return temp[target]