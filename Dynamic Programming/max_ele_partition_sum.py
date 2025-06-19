def max_ele_partition_sum(i,arr,k):
    n = len(arr)
    if i == n:
        return 0

    length= 0
    cur_max = float('-inf')
    maxi = float('-inf')

    for j in range(i,min(i+k,n)):  ## idx can be out of bounds
        length += 1 # keep length track
        cur_max = max(cur_max,arr[j])

        cost = length * cur_max + max_ele_partition_sum(j+1,arr,k)
        maxi = max(mini,cost)
    
    return maxi

def tabular(arr,k):
    n = len(arr)
    dp = [float('inf') for _ in range(n)]
    dp[n-1] = 0

    for i in range(n-2,-1,-1):

        length= 0
        cur_max = float('-inf')
        maxi = float('-inf')

        for j in range(i,min(i+k,n)):  ## idx can be out of bounds

            length += 1 # keep length track
            cur_max = max(cur_max,arr[j])

            cost = length * cur_max + dp[j+1]
            maxi = max(mini,cost)
        
        dp[i] = maxi
    
    return dp[0]