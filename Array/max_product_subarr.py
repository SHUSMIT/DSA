def maximum_product_subarr(arr):
    prefix = 1
    suffix = 1
    maxi = float('-inf')
    n = len(arr) 
    for i in range(n):
        prefix *= arr[i] # front
        suffix *= arr[n-i-1] #back
        maxi = max(maxi,prefix,suffix)

        if prefix == 0:
            prefix = 1 # reintialise to 1 as it has become 0
        if suffix == 0:
            suffix = 1
    
    return maxi
        
