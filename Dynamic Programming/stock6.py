## transaction fee now
def stock6(idx,buy,arr,fee): ## unlimted stock question
    # 0 toward n
    if idx == len(arr):
        return 0 # exhausted

    # buy
    if buy:
        take = -arr[idx] + stock6(idx+1,0,arr,fee) 
        not_take = 0 + stock6(idx+1,1,arr,fee)
        profit = max(take,not_take)

    else: #sell, then go two ahead due to cooldown
        sell = arr[idx] - fee + stock6(idx+1,1,arr,fee) # for complete 
        not_sell = 0 + stock6(idx+1,0,arr,fee)
        profit = max(sell,not_sell)

    return profit

def tabular(arr,fee):
    n = len(arr)
    dp = [[0 for _ in range(2)] for _ in range(n+1)]

    # go n -> 0
    for i in range(n-1,-1,-1):
        for j in range(2):

            if j:
                take = -arr[i] + dp[i+1][0]
                not_take = 0 + dp[i+1][1]
                dp[i][j] = max(take,not_take)

            else: #sell, fee for complete
                sell = arr[i] + dp[i+1][1] - fee
                not_sell = 0 + dp[i+1][0]
                dp[i][j] = max(sell,not_sell)

    return dp[0][1]
