def stock3(idx,buy,arr,limit):
    if idx == len(arr): #exhausted
        return 0
        
    if linit ==0:
        return 0
    
    
    if buy: # can buy
        take = -arr[idx] + stock2(idx+1,0,arr,linit)
        not_take = 0 + stock3(idx+1,1,arr,linit)
        profit = max(take,not_take)
    
    else: ## cant buy, sell or not
        sell = arr[idx] + stock3(idx+1,1,arr,limit-1) ## limit reduce as complete transaction done
        not_sell = 0 + stock3(idx+1,0,arr,limit)
        profit = max(sell,not_sell)
    
    return profit

def memoise(idx,buy,arr,limit,dp):
    ## 0 toward n
    if idx == len(arr): #exhausted
        return 0
    if limit ==0: ## max transaction exceeeded
        return 0
    
    if dp[idx][buy][limit] != -1:
        return dp[idx][buy][limit]
    
    if buy: # can buy
        take = -arr[idx] + memoise(idx+1,0,arr,limit,dp)
        not_take = 0 + memoise(idx+1,1,arr,limit,dp)
        dp[idx][buy][limit] = max(take,not_take)
    
    else: ## cant buy, sell or not
        sell = arr[idx] + memoise(idx+1,1,arr,limit,dp)
        not_sell = 0 + memoise(idx+1,0,arr,limit,dp)
        dp[idx][buy] = max(sell,not_sell,limit,dp)
    
    return dp[idx][buy][limit]

def tabular(arr,limit):
    n = len(arr)
    dp = [ [0 for _ in range(limit) ] for  _ in range(2)] for _ in range(n+1) ]  ## dp[idx][buy][limit]
    
    # cap = 0, then idx, buy anything --> 0
    # idx = n, then cap, buy anything -- > 0
    
    # for i in range(n+1):
    #     for j in range(2):
    #         dp[i][j][0] = 0
    
    # for j in range(2):
    #     for k in range(limit):
    #         dp[n][j][k] = 0
    
    ## go from n toward 0 now
    
    for i in range(n-1,-1,-1):
        for buy in range(0,2):
            for k in range(1,limit): ## cap 0 is 0 only
                
                if buy: # can buy
                    take = -arr[idx] + dp[idx+1][0][k]
                    not_take = 0 + dp[idx+1][1][k]
                    dp[idx][buy][k] = max(take,not_take)
                
                else: ## cant buy, sell or not
                    sell = arr[idx] + dp[idx+1][1][k-1]
                    not_sell = 0 + dp[i][0][k]
                    dp[idx][buy][k] = max(sell,not_sell,limit,dp)
    
    return dp[n][1][limit-1]


def space_optimal(arr):
    n = len(arr)
    dp = [0 for _ in range(limit) ] for  _ in range(2)] # prev[buy][limit]
    
    # cap = 0, then idx, buy anything --> 0
    # idx = n, then cap, buy anything -- > 0
    
    # for i in range(n+1):
    #     for j in range(2):
    #         prev[j][0] = 0
    
    # for j in range(2):
    #     for k in range(limit):
    #         prev[j][k] = 0
    
    ## go from n toward 0 now
    
    for i in range(n-1,-1,-1):
        curr = [0 for _ in range(limit) ] for  _ in range(2)] 
        for buy in range(0,2):
            for k in range(1,limit):
                
                if buy: # can buy
                    take = -arr[i] + prev[0][k]
                    not_take = 0 + prev[1][k]
                    curr[buy][k] = max(take,not_take)
                
                else: ## cant buy, sell or not
                    sell = arr[i] + prev[1][k-1]
                    not_sell = 0 + prev[0][k]
                    curr[buy][k] = max(sell,not_sell,limit,dp)
                    
        curr = prev
        
    return prev[1][limit-1]
    
            