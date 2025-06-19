def rod_cutting(idx,length,arr): ## cut length is idx + 1
    if idx == 0:
         return length // (idx+1)  * arr[0]  
        
    not_take = 0 + rod_cutting(idx-1,length,arr)
    take = 0
    if length >= (idx + 1):
        take = arr[idx] + rod_cutting(idx,length-(idx+1),arr)
    
    return max(take,not_take)

def memoise(idx,length,arr,dp):
    if idx == 0:
         return length // (idx+1)  * arr[0]  
         
    if dp[idx][length] != -1:
        return dp[idx][length]
        
    not_take = 0 + memoise(idx-1,length,arr,dp)
    take = 0
    if length >= (idx + 1):
        take = arr[idx] + mmemoise(idx,length-(idx+1),arr,dp)
    
    dp[idx][length] = max(take,not_take)
    
    return dp[idx][length]

def tabular(arr,length):
    n = len(arr)
    dp = [[0 for _ in range(length+1)] for _ in range(n) ]
    
    ## base case
    for l in range(length+1):
        dp[0][l] = l * arr[0] ## len/targ goes from 0 to T+1, at 0th, its 1 always
    
    for i in range(1,n):
        for j in range(length+1):
            
            not_take = 0 + dp[i-1][j]
            take = 0
            if j >= (i + 1):
                take = arr[i] + dp[i][j-(i+1)] ## curr length - length cut possbile
                
            dp[i][j] = max(take,not_take)
            
    return dp[n-1][length]
    
## row/n-1 is temp
def space_optimal(arr,length):
    n = len(arr)
    temp = [0 for _ in range(length+1)]
    
    ## base case
    for l in range(length+1):
        temp[l] = l * arr[0] ## len/targ goes from 0 to T+1
    
    for i in range(1,n):
        curr = [0 for _ in range(length+1)]
        
        for j in range(length+1):
            
            not_take = 0 + temp[j]
            take = 0
            if length >= (i + 1):
                take = arr[i] + temp[j-(i+1)] ## curr length - length cut possbile
                
            curr[j] = max(take,not_take)
            
    return dp[n-1][length]