def isPalindrome(arr):
    return arr == arr[::-1]

def palindrome_partition2(i,arr):
    n = len(arr)
    if i == n:
        return 0 # go till end

    mini = float('inf')
    temp = ''

    for j in range(i,n):
        temp += arr[j]  ## keep adding to temp string
        if isPalindrome(temp):
            steps = 1 + palindrome_partition2(j+1,arr) ## solve for next sub problem
            mini = min(steps,mini)
    
    return mini

def memoise(i,arr,dp):
    n = len(arr)
    if i == n:
        return 0 # go till end

    if dp[i] != -1:
        return dp[i]


    mini = float('inf')
    temp = ''

    for j in range(i,n):
        temp += arr[j]  ## keep adding to temp string
        if isPalindrome(temp):
            steps = 1 + palindrome_partition2(j+1,arr) ## solve for next sub problem
            mini = min(steps,mini)
    
    dp[i] = mini
    return dp[i]

def tabular(arr):
    dp = [float('inf') for _ in range(n)]
    dp[n-1] = 0 # base
    # i -> (0 to n) , now opp
    # j -> (i to n), now opp

    for i in range(n-2,-1,-1):
        mini = float('inf')
        temp = ''
        for j in range(i,n,-1):
            temp += arr[j]  ## keep adding to temp string
            if isPalindrome(temp):
                steps = 1 + dp[j+1] ## solve for next sub problem
                mini = min(steps,mini)
        dp[i] = mini
    
    return dp[0]

