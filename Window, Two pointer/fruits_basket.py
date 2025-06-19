def fruits_basket(arr,k): # k : baskets/variety
    l,r = 0,0 
    num_freq = dict()
    maxi = 0
    n = len(arr)

    while r < n:

        if arr[r] not in num_freq: # not present, add
            num_freq[arr[r]] = 1 # initalise with 1 

        elif arr[r] in num_freq:
            num_freq[arr[r]] += 1 # kepp increase frequency 

        while len(num_freq) > k: # not valid, move left, and decrement

            num_freq[arr[l]] -= 1 
            if num_freq[arr[l]] == 0: # if 0 , remove it from dict

                del(num_freq[arr[l]]) 

            l += 1 # shrink

        if len(num_freq) <= k: # valid            
            maxi = max(maxi, r-l+1)
        
        r += 1

    return maxi