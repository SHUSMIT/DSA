def longest_sumk(arr,k):
    n = len(arr)
    l,r =0,0
    maxi = 0
    l_id,r_id = -1,-1
    curr_sum = 0

    while r < n:

        curr_sum += arr[r] ## add it
        
        while curr_sum > k: # invalid

            curr_sum -= arr[l]
            l += 1 ## shrink
        
        if curr_sum <= k:
            if r-l+1 >  maxi: # curr length is more
                maxi = r-l+1
                r_id,l_id = r,l # store the index
        
        r +=1 # expand


    return maxi,arr[l_id:r_id+1]


arr = [1, 2, 1, 0, 1, 1, 0]
k = 4
length, subarray = longest_sumk(arr, k)
print("Length:", length)
print("Subarray:", subarray)
