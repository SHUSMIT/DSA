def max_sum_subsequence(idx,arr):
    if idx == 0:
        return arr[idx] ## means 1 is not picked, i want to maximise
    if idx < 0:
        return 0 ## if idx = 1, idx-2 would mean out of bound
    
    pick = arr[idx] + max_sum_subsequence(idx-2, arr) ## picked arr[idx] so now idx-2 can be possibility 
    not_pick = 0 + max_sum_subsequence(idx-1, arr) ## not picked idx, so idx-1 can be apossibility
    return max(pick,not_pick)  ## pick,not pick question

def memoise(idx,arr,dp):
    if idx == 0:
        return arr[idx]
    
    if idx < 0:
        return 0
    
    if dp[idx] != -1:
        return dp[idx] 

    pick = arr[idx] + memoise(idx-2, arr, dp) ## picked arr[idx] so now idx-2 can be possibility 
    not_pick = 0 + memoise(idx-1, arr , dp ) ## not picked idx, so idx-1 can be apossibility
    dp[idx] = max(pick,not_pick)

    return dp[idx]


def tabular(arr,dp):
    ## bootom top 
    dp[0] = arr[0]
    for i in range(1,len(arr)):

        pick = arr[i] 

        if i > 1:
            pick += dp[i-2]  ## picked i 

        not_pick = 0 + dp[i-1] ## not picked i

        dp[i]  = max(pick,not_pick)

    return dp[len(arr)-1]  


def optimised(arr):    ### prev2  prev   curr
    prev = arr[0]         ### i-2     i-1     i 
    prev2 = 0

    for i in range(1,len(arr)):

        pick = arr[i]

        if i>1:
            pick += prev2
        
        not_pick = 0 + prev
        curr = max(pick,not_pick)

        prev2 = prev
        prev = curr
    
    return prev







arr = [2, 1, 4, 9]
n = len(arr)
dp = [-1] * n

print("Recursion:", max_sum_subsequence(n - 1, arr))
print("Memoization:", memoise(n - 1, arr, dp))
print("Tabular:", tabular(arr,dp))
print("Optimised:", optimised(arr))


