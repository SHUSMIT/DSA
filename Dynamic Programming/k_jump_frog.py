def frong_k_jump(idx,arr,k):
    if idx == 0:
        return 0

    ## jump i to i-k
    min_energy = float('inf')
    ## observe that idx is constant 1 -- K is changing
    for i in range(1,k):
        if idx - i >= 0:
            curr_energy = frong_k_jump(idx-k) + abs(arr[idx] - arr[idx-k])
            min_energy = min(min_energy,curr_energy) ## instead of l,r its looped

    return min_energy

def memoize(arr,k,dp):
    if idx == 0:
        return 0
    
    min_energy = float('inf')

    if dp[idx] != -1:
        return dp[idx] ## memoised

    for i in range(1,k):
        if idx - i > 0;
        curr_energy = dp[idx-i] + abs(arr[idx] - arr[idx-i] )
        min_energy = min(curr_energy,min_energy)
    
    return min_energy


def tabulated(arr,k,dp):
    dp[0] = 0

    for i in range(1,n):
        min_energy = float('inf')
        ## steps
        for j in range(1,k):
            if i-j >= 0:
                curr_energy = dp[idx-k] + abs(arr[idx] - arr[idx-k])
                min_energy = min(min_energy,curr_energy)

        dp[i] = min_energy ## store the min ebergy

    return dp[len(arr)-1]


