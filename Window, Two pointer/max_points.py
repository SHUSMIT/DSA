def max_points(arr,k):

    n = len(arr)
    if k == 0:
        return 0

    lsum,rsum,maxi=0,0,0

    lsum = sum(arr[:k]) ## sum of first k elements

    maxi = lsum
    r_idx = n-1
    # i goes from k-1 to 0 and r from n-1 towards n-1-k 
    for i in range(k-1,-1,-1): 
        lsum -= arr[i]
        rsum += arr[r_idx]
        r_idx -= 1 # start increasing right portion also
        maxi = max(maxi,lsum+rsum)
    
    return maxi
