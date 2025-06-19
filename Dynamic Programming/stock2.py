def stock2(idx,buy,arr):
    if idx == len(arr): #exhausted
        return 0
    
    if buy: # can buy
        take = -arr[idx] + stock2(idx+1,0,arr)
        not_take = 0 + stock2(idx+1,1,arr)
        profit = max(take,not_take)
    
    else: ## cant buy, sell or not
        sell = arr[idx] + stock2(idx+1,1,arr)
        not_sell = 0 + stock2(idx+1,0,arr)
        profit = max(sell,not_sell)
    
    return profit

def memoise(idx,buy,arr,dp):
    ## 0 toward n
    if idx == len(arr): #exhausted
        return 0
    
    if dp[idx][buy] != -1:
        return dp[idx][buy]
    
    if buy: # can buy
        take = -arr[idx] + memoise(idx+1,0,arr)
        not_take = 0 + memoise(idx+1,1,arr)
        dp[idx][buy] = max(take,not_take)
    
    else: ## cant buy, sell or not
        sell = arr[idx] + memoise(idx+1,1,arr)
        not_sell = 0 + memoise(idx+1,0,arr)
        dp[idx][buy] = max(sell,not_sell)
    
    return dp[idx][buy]

def tabular(arr):
    n = len(arr)
    dp = [ [-1 for  _ in range(3)] for _ in range(n+1) ]  ## dp[idx][buy]
    
    dp[n][0] = dp[n][1] = 0
    ## go from n toward 0 now
    
    for i in range(n-1,-1,-1):
        for buy in range(0,2):
            
            if buy: # can buy
                take = -arr[i] + dp[i+1][0]
                not_take = 0 + dp[i+1][1]
                dp[i][buy] = max(take,not_take)
            
            else: ## cant buy, sell or not
                sell = arr[i] + dp[i+1][1]
                not_sell = 0 + dp[i+1][0]
                dp[i][buy] = max(sell,not_sell)
    
    return dp[0][1]

def space_optimal(arr):
    n = len(arr)
    prev = [-1 for  _ in range(2)]
    
    prev[0] = prev[1] = 0
    ## go from n toward 0 now
    
    for i in range(n-1,-1,-1):
        
        curr = [-1 for _ in range(2)]
        for buy in range(0,2):
            
            if buy: # can buy
                take = -arr[i] + prev[0]
                not_take = 0 + prev[1]
                curr[buy] = max(take,not_take)
            
            else: ## cant buy, sell or not
                sell = arr[i] + prev[1]
                not_sell = 0 + prev[0]
                curr[buy] = max(sell,not_sell)
                
        prev = curr
        
    return prev[1]
    
            