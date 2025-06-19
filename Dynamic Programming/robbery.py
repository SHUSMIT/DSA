def ninja(day,mat,last): ## idx -> day
    cur_max = 0
    if day == 0: ## last base case
        for i in range(3):
            if day != last:
                cur_max = max(cur_max,mat[day][i])
    
    final_max = 0
    ## now for all other cases
    for i in range(3):
        if i != last: ## the last cant be repeated
            curr = arr[day][i] + ninja(day-1,mat,i) ## i want to get all the combination, so for each day 
            final_max = max(cur,final_max) ## recurse and check cur_max, calling for day-1 does it for all possible combination
    
    return final_max

def memoize(day,mat,last,dp):
    cur_max = 0
    if day == 0: ## last base case
        for i in range(3):
            if day != last:
                cur_max = max(cur_max,mat[day][i],dp)
    
    if dp[day][last] != -1:
        return dp[day][last]
    
    final_max = 0
    ## now for all other cases

    for i in range(3):
        if i != last: ## the last cant be repeated
            curr = arr[day][i] + memoize(day-1,mat,i) ## i want to get all the combination, so for each day 
            dp[day][i] = max(cur,final_max) ## recurse and check cur_max, calling for day-1 does it for all possible combination
    
    return dp[day][last]


def tabulation(day,mat,prev,dp):
    ## first the base condition, dp[day][next]
    dp[0][0] = max(dp[0][1],d[0][2])
    dp[0][1] = max(dp[0][0],d[0][2])
    dp[0][2] = max(dp[0][1],d[0][0])

    ## next loop 
    for day in range(1,len(mat)):
        for last in range(4):
            dp[day][last] = 0 ## update it later
            for task in range(3):
                curr = mat[day][task] + dp[day-1][task] ## previous days 
                dp[day][last] = max(curr, dp[day][last]) # update it now

    return dp[n-1][3]



    
    

