def subset_partition(arr):
    target = sum(arr)
    if  target% 2: ## sum is odd
        return False
    return partition(arr,target//2)
    
def partition(idx,arr,target):
    ## we come toward 0 index, 0 target
    if target == 0:
        return True
    if idx == 0:
        return a[0] == target
    
    not_take = partition(idx-1,arr,target)
    take False
    if target >= arr[idx]:
        take = partition(idx-1,arr,target-arr[idx])
    
    return take or not_take

def memo(idx,arr,target,dp):
    ## we come toward 0 index, 0 target
    if target == 0:
        return True
    if idx == 0:
        return a[0] == target
        
    ## dp[idx][target]
    if dp[idx][target] != -1:
        return dp[idx][target]
        
    not_take = partition(idx-1,arr,target)
    take False
    if target >= arr[idx]:
        take = partition(idx-1,arr,target-arr[idx])
    
    dp[idx][target] = take or not_take
    
    return dp[idx][target]

def tabular(arr):
    dp = [-1 for P in range(target) for in range(len(arr))]
    
    for i in range(len(arr)):
        dp[i][0] = True
    for i in range(len(arr)):
        dp[0][i]] = True
    ## now go 1 to n-1 for each 
    for i in range(1,len(arr)):
        for j in range(1,len(arr)):
            
                not_takev = dp[i][j
                take False
                if target >= arr[i]:
                    take = dp[i][j]
                
                dp[i][j]= take or not_take
                
    return dp[len(arr)-1][target]
                    
        