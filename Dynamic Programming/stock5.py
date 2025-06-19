## cooldown now, immediate buy not possible
def stock5(idx,buy,arr): ## unlimted stock question
    # 0 toward n
    if idx == len(arr):
        return 0 # exhausted

    # buy
    if buy:
        take = -arr[idx] + stock5(idx+1,0,arr) 
        not_take = 0 + stock5(idx+1,1,arr)
        profit = max(take,not_take)

    else: #sell, then go two ahead due to cooldown
        sell = arr[idx] + stock5(idx+2,1,arr)
        not_sell = 0 + stock5(idx+1,0,arr)
        profit = max(sell,not_sell)

    return profit

def tabular(arr):
    n = len(arr)
    dp = [[0 for _ in range(2)] for _ in range(n+2)]

    # go n -> 0
    for i in range(n-1,-1,-1):
        for j in range(2):

            if j:
                take = -arr[i] + dp[i+1][0]
                not_take = 0 + dp[i+1][1]
                dp[i][j] = max(take,not_take)

            else: #sell, then go two ahead due to cooldown
                sell = arr[i] + dp[i+2][1]  ## n+2 for out of ound safety
                not_sell = 0 + dp[i+1][0]
                dp[i][j] = max(sell,not_sell)

    return dp[0][1]
