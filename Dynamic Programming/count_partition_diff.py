def count_partition(arr, diff):
    S = sum(arr)
    
    # Check for valid (S - diff)
    if (S - diff) < 0 or (S - diff) % 2 != 0:
        return 0

    target = (S - diff) // 2
    zero_count = arr.count(0)

    # Use tabular approach
    count = tabular(arr, target)

    # Include 2^zero_count combinations
    return count * pow(2, zero_count)
    
    
def count_sum_k(idx,target,arr):
    if target == 0:
        return 1 ## got one
    if idx == 0:
        if arr[0] == target:
            return 1 ## the last element can satisfy target
        else:
            return 0 
    
    not_take = count_sum_k(idx-1,target,arr)
    take = 0
    if target >= arr[idx]:
        take = count_sum_k(idx-1,target-arr[idx],arr)
    
    return take + not_take

def memoise(idx,target,dp,arr):
    if target == 0:
        return 1 ## got one
    if idx == 0:
        if arr[0] == target:
            return 1 ## the last element can satisfy target
        else:
            return 0 
    
    if dp[idx][target] != -1:
        return dp[idx][target]
    
    not_take = memoise(idx-1,target,dp,arr)
    take = 0
    if target >= arr[idx]:
        take = memoise(idx-1,target-arr[idx],dp,arr)
    
    dp[idx][target] = take + not_take
    
    return dp[idx][target]

def tabular(arr,target):
    n = len(arr)
    dp = [0 for _ in range(target+1) ] for _ in range(n)] ## dp[idx][target]
    
    ## base case
    for i in range(n):
        dp[i][0] = 1 ## target = 0 so done
    
    if arr[0] <= target:
        dp[0][arr[0]] = 1  # base case: one way if arr[0] == target

    
    ## go 0 toward n
    for i in range(1,n):
        for j in range(1,target+1):
            
            not_take = dp[i-1][j]
            take = 0
            if j >= arr[i]:
                take = dp[i-1][j-arr[i]]
                
            dp[i][j] = take + not_take
    
    return dp[n-1][target]
    
    