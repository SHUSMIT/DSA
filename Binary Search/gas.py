import math 

def count_station(arr,dist):
    count = 0
    for i in range(1, len(arr)):
        gap = arr[i] - arr[i-1]
        # Number of stations needed in this segment
        count += int(math.ceil(gap / dist)) - 1
    return count
 
def gas_station(arr,k): ##k is the number to be placed
    low = 0
    high = 0
    
    for i in range(1,len(arr)):
        high = max(high,arr[i]-arr[i-1])
        
    tol = 1e-6
    
    while (high-low >= tol):
        mid = (low+mid)/2 ##not // 
        count = count_station(arr,mid)
        if count > k:  ## more required to be placed so shrink , ie, increase
            low = mid
        else:
            ans = high
            high = mid
    
    return ans
            
    