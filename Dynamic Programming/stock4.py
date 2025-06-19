def maxProfit(k, prices):
    n = len(prices)
    if n == 0 or k == 0:
        return 0

    # If k is large, use the greedy solution for unlimited transactions
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

    # DP table: dp[transactions][day]
    dp = [[0] * n for _ in range(k + 1)]

    for t in range(1, k + 1):
        max_diff = -prices[0]
        for day in range(1, n):
            # Either don't trade today, or sell today (and buy at some previous point)
            dp[t][day] = max(dp[t][day - 1], prices[day] + max_diff)
            # Update max_diff for the next day
            max_diff = max(max_diff, dp[t - 1][day] - prices[day])

    return dp[k][n - 1]
