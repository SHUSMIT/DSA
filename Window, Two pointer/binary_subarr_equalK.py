def binary_subarr_equalK(arr,k):
    return binary_subarr_less_k(arr,k) - binary_subarr_less_k(arr,k-1)

def binary_subarr_less_k(arr,k):

    if k < 0:
        return 0

    number = 0
    curr_sum = 0
    l,r = 0,0

    while r < n:
        curr_sum += arr[r]

        while curr_sum > k: ## invalid
            curr_sum -= arr[l] # remove l
            l += 1 # shrink
        
        length = r-l+1 ## itself and before all, so length
        number += length # this considers all combination with sum <= k (not equal exact)

        r += 1 # expand
    
    return curr_sum