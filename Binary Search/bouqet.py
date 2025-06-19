def isValid(arr,m,k,mid):
    total = 0
    for i in range(len(arr)):
        
        if arr[i] <= mid:
            count +=1
        else:
            total += (count//k)  ## number of adjacent/ required number of adajacent
            count = 0
            
    total += (count//k)
    
    return total >= m
    
#m is number of boquet and k is number of adjacent flower

def bloom(arr,m,k):
    
    if m*k > len(arr):
        return -1
    
    low, high = min(arr), max(arr)
    ans = -1
    
    while low<=high:
        
        mid = (low+high)//2
        if (isValid(arr,m,k,mid)):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans
 