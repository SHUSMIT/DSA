def number_of_subseq(arr):
    n = len(arr)
    dp = [1 for _ in range(n)]
    count = [1 for _ in range(n)] ## initally all self seq

    for i in range(n):
        for j in range(i):

            if arr[i] > arr[j] and dp[i] < 1 + dp[j]: ## its increase, so increase length and copy the possible subseq
                dp[i] = 1 + dp[j] # update it
                count[i] = count[j] # copy it

            elif arr[i] > arr[j] and dp[i] == 1 + dp[j]: ## another element found which when added + 1 gives same length, we skipped it earlier here add it
                count[i] += count[j] # add it as it could have alterante possible paths

    val = max(dp)
    total = sum(count[i] for i in range(n) if dp[i] == val ) 
    return total