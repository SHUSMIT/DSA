def longest_increasing_subseq(idx,prev_idx,arr): ## 0 toward n, increasing seq

    if idx == len(arr): #exhasuted
        return 0

    if prev_idx == -1 or arr[prev_idx] < arr[idx]: # can take:
        take = 1 + longest_increasing_subseq(idx+1,idx,arr) # take it, update
        not_take = longest_increasing_subseq(idx+1,prev_idx,arr) # keep checking for better

        return max(take,not_take)

    else:
        return longest_increasing_subseq(idx+1,prev_idx,arr)


## prev_idx is right shifted by one, so prev_idx + 1 as -1 was there
def memoise(idx, prev_idx, arr, dp):
    if idx == len(arr):  # Exhausted
        return 0

    if dp[idx][prev_idx + 1] != -1:  # Use prev_idx + 1 to handle -1
        return dp[idx][prev_idx + 1]

    if prev_idx == -1 or arr[prev_idx] < arr[idx]:  # can take

        take = 1 + memoise(idx + 1, idx, arr, dp)  
        not_take = memoise(idx + 1, prev_idx, arr, dp) 

        dp[idx][prev_idx + 1] = max(take, not_take)
        return dp[idx][prev_idx + 1]

    else:
        dp[idx][prev_idx + 1] = memoise(idx + 1, prev_idx, arr, dp)  
        return dp[idx][prev_idx + 1]



def tabular(arr):
    n = len(arr) 
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)] # n*n, base case handles n

    # go from n + 1 towards 0 
    for idx in range(n-1,-1,-1):
        for prev_idx in range(idx-1,-2,-1):  # idx-1 to -1 inclusive (+1 shift) .. whenever dp, coordinate shift to be done

            if prev_idx == -1 or arr[prev_idx] < arr[idx]:  # can take

                take = 1 + dp[idx + 1][idx + 1] 
                not_take = dp[idx + 1][prev_idx + 1] # adjust +1 

                dp[idx][prev_idx + 1] = max(take, not_take)
                

            else:
                dp[idx][prev_idx + 1] = dp[idx + 1][prev_idx + 1]  

    return dp[0][0]


def space_optima(arr):
    n = len(arr) 
    prev = [0 for _ in range(n+1)] # n*n, base case handles n

    # go from n + 1 towards 0 
    for idx in range(n-1,-1,-1):
        curr = [0 for _ in range(n+1)]

        for prev_idx in range(idx-1,-2,-1):  # idx-1 to -1 inclusive (+1 shift) .. whenever dp, coordinate shift to be done

            if prev_idx == -1 or arr[prev_idx] < arr[idx]:  # can take

                take = 1 + prev[idx + 1] 
                not_take = prev[prev_idx + 1] # adjust +1 

                curr[prev_idx + 1] = max(take, not_take)
                

            else:
                curr[prev_idx + 1] = prev[prev_idx + 1]  

    return prev[0]


def better_table(arr):
    n = len(arr)
    dp = [0 for _ in range(n)] ## dp[i] tells the max subseq length using ith 

    for i in range(n): 
        for prev in range(i): ## i check every prev
            if arr[prev] < arr[i]: #satisfy
                length = 1 + dp[prev] # attach 
                dp[i] = max(dp[i] , length) # only if better, update
    
    return max(dp)


