def frog_jump(idx,arr):
if idx == 0: ## on idx
    return 0

left = frog_jump(idx-1, arr) + abs(arr[idx-1] - arr[idx])
if idx > 1:
    right = frog_jump(idx-2, arr) + abs(arr[idx-2] - arr[idx])
else:
    right = float('inf')

return min(left,right)

## memoise the parameters changing
## index is changing
def memoise(idx, arr, dp_arr):
    if idx == 0:
        return 0

    if dp_arr[idx] != -1:
        return dp_arr[idx]

    left = memoise(idx - 1, arr, dp_arr) + abs(arr[idx] - arr[idx - 1])
    right = float('inf')

    if idx > 1:
        right = memoise(idx - 2, arr, dp_arr) + abs(arr[idx] - arr[idx - 2])

    dp_arr[idx] = min(left, right) ## memoise

    return dp_arr[idx]


def tabulation(idx,arr,dp): ## bottom to up
    dp[0] = 0
    
    for idx in range(1,len(arr)):
        left = dp[idx-1] + abs(arr[idx] - arr[idx-1])
        if idx  > 1:
            right = dp[idx-2] + abs(arr[idx] - arr[idx])
        else:
            right = float('inf')

        dp[idx] = min(left,right)
    
    return dp[n-1]


def space_optimised(idx,arr):
    prev = 0
    prev2 = 0

    for i in range(1,len(arr)):
        
        left = prev + abs(arr[i] - arr[i-1])
        if i>1:
            right = prev2 + abs(arr[i] - arr[i-1])
        else:
            right = float('inf')
        
        curr = min(left,right)

        prev = curr  ## now index would change after iteration, prev becomes curr, prev2 becomes prev
        prev2 = prev
