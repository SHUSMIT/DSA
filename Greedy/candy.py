def candy(rating):
    n = len(rating)

    ans = [1 for _ in range(n)]

    #go from 0 to n-1
    for i in range(1,n):
        if rating[i] > rating[i-1]: # right (i) > left (i-1)
            ans[i] = ans[i-1] + 1 # one more than it
    
    #go from n-1 to 0
    for i in range(n-1,0,-1):
        if rating[i] < rating[i-1]:
            val = 1 + ans[i]
            ans[i-1] = max(ans[i-1] ,val)
    
    return sum(ans)

def slope_approach(rating):
    n = len(rating)
    if n == 0:
        return 0

    val = 1  # First child always gets one candy
    i = 1

    while i < n:
        # Plateau (equal ratings)
        if rating[i] == rating[i-1]:
            val += 1
            i += 1
            continue

        # Upslope (increasing)
        up = 0
        while i < n and rating[i] > rating[i-1]:
            up += 1
            val += up + 1 if up == 1 else 1  # Give one more on first up, then 1 each step
            i += 1

        # Downslope (decreasing)
        down = 0
        while i < n and rating[i] < rating[i-1]:
            down += 1
            val += down
            i += 1

        # If the down slope is longer than the up slope, need to give extra to the peak
        if down > up:
            val += down - up

    return val
