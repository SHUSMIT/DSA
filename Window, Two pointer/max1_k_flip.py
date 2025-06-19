def max1_k_flip(arr,k):
    n = len(arr)
    l,r = 0

    countk = 0
    curr_length = 0
    maxi = float('-inf')

    while r < n:

        if arr[r] == 0: # if zero, increase count
            countk += 1
        
        while countk > k: # till zeros exceed

            if arr[l] == 0:  # 0 encounter by left
                countk -= 1 # reduce
            
            l += 1      # move left forward
        
        if countk <= k:    # for valid countk

            curr_length = r-l+1
            maxi = max(maxi,curr_length) 
        
        r += 1
    
    return maxi

    