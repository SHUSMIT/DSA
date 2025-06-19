import math

def isValid(arr,i,h):
    
    return h >= sum([math.ceil(x/i) for x in arr])

def koko(arr,n,h):
    
    low,high = 1, arr[n-1]
    ans = high
    
    while low<=high:
        mid = (low+high)//2
        ## valid region
        if isValid(arr,mid,h):
            ans = mid
            high = mid - 1
        
        else:
            low = mid + 1
        
    return ans
        
            