def lonegest_divisible(arr):
    n = len(arr)
    parent = [i for i in range(n)]
    dp = [1 for i in range(n)]
    arr.sort()

    for  i in range(n):
        for j in range(i): 
            if arr[i] % arr[j] == 0: # prev divisble 
                length = 1 + dp[j] # increase length of subseq
                if length >= dp[i]:
                    dp[i] = length # update length of longest seq
                    parent[i] = j # store the parent
    

    ans = []
    i = dp.index(max(dp)) # index of max element in dp
    while parent[i] != i:
        ans.append(arr[i])
        i = parent[i]
    ans.append(arr[i]) # add the last 

    return ans[::-1]