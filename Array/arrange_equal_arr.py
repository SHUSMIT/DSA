def arrange_equal_arr(arr):
    n =len(arr)
    ans = [-1 for _ in range(n)]

    pos_id = 0
    neg_id = 1
    
    for i in range(n):

        if arr[i] > 0:  # Positive number
            ans[pos_id] = arr[i]
            pos_id += 2  # Move to next even index

        else:  # Negative number
            ans[neg_id] = arr[i]
            neg_id += 2  # Move to next odd index

    return ans

def arrange_equal(arr):
    n = len(arr)

    positive = []
    negative = []

    for i in range(n):
        if arr[i] < 0:
            negative.append(arr[i])
        else:
            positive.append(arr[i])
    

    m,n = len(positive),len(negative)
    ans = []
    if m > n: # more posive 
        for i in range(n):
            ans.append(positive[i])
            ans.append(negative[i]) # alterate

        ans.extend(positive[n:])

    else:
        for i in range(m):
            ans.append(positive[i])
            ans.append(negative[i])

        ans.extend(negative[m:])
    
    return ans
