def median_two_sorted(arr,brr):
    n = len(arr)
    m = len(brr)
    
    if n>m:
        return median_two_sorted(brr,arr) ##i want arr to be shorter
    
    low = 0
    high = n
    left = (m+n+1)//2
    
    ##iterate through smaller, finding out how many to be taken
    
    while(low <= high):
        
        mid1 = (low+high)//2
        mid2 = left - mid1
        l1,l2,r1,r2 = float('-inf'),float('-inf'),float('inf'),float('inf')
        
        if(mid1 < n):
            r1 = arr[mid1]  ## check if valid on right
        if(mid2 < m):
            r2 = brr[mid2]
        if(mid1-1) >= 0: ##check if left present
            l1 = arr[mid1 - 1]
        if(mid2-1) >= 0:
            l2 = brr[mid2 - 1]
        if(l1 <= r2) and (l2<=r1): ##found the valid
            if(n+m) %2 == 0:
                return (max(l1,l2) + min(r1,r2))/2
            else:
                return max(l1,l2)
        
        if(l1 > r2):
            high = mid1 - 1 ## we have to go lefter so that bigger element not present
        else:
            low = mid1 + 1
    
    return 0
        
    
    
    
    