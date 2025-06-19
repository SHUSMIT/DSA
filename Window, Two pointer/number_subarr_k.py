def number_subarr_k(arr,k):
    prefix_sum = dict()
    count = 0
    pre_sum = 0
    
    prefix_sum[0] = 1
    ## hash stores ( prefix_sum , count )

    for i in range(len(arr)):
        pre_sum += arr[i]
        if pre_sum - k in prefix_sum: ## x-k is in hash map
            count += prefix_sum[pre_sum-k] ## add the occurences of x-k 
        
        if pre_sum not in prefix_sum:
            prefix_sum[pre_sum] = 1
        else:
            prefix_sum[pre_sum] += 1
    
    return count