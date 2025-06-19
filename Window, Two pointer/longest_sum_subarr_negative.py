def longest_sub_sumK_negative(arr,k):
    #as -ve, hashing req
    prefix_sum = dict()
    maxi = 0
    pre_sum = 0

    for i in range(len(arr)):
        pre_sum += arr[i]
        
        # If subarray from index 0 to i has sum k
        if pre_sum == k:
            length = i + 1
            maxi = max(maxi,length)

        if pre_sum - k in prefix_sum: #(x-k) exist, so definitely k is there
            length = i - prefix_sum[pre_sum-k] 
            maxi = max(maxi,length)

        if pre_sum not in prefix_sum:
            prefix_sum[pre_sum] = i # store the index of prefix sum's first occur only 
    
    return maxi

