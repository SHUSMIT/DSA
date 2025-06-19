def stock1(arr):
    min_price = arr[0] # first element
    max_profit = 0
    
    for price in arr:
        min_price = min(min_price,price) ## find the minimal as you iterate
        max_profit = max(max_profit, price - min_price) # assume we sell the stock on current day
    
    return max_profit
        