def lower_bound(arr,x):
    low,high = 0, len(arr) - 1
    ans = len(arr)

    
    while (low<=high):
        mid = (low+high)//2
        if arr[mid] == x:
            return ans
        
        elif arr[mid] < x: ## chane space as no prob of answer
            low = mid + 1
        
        elif arr[mid] >= x:  ##  find some better value. current val is possible as val >= x
            ans = mid
            high = mid - 1
    
    return ans

def upper_bound(arr,x):
    low,high = 0, len(arr) - 1
    ans = len(arr)

    
    while (low<=high):
        mid = (low+high)//2
        
        elif arr[mid] < x: ## chane space as no prob of answer
            low = mid + 1
        
        elif arr[mid] > x:  ##  find some better value. current val is possible as val >= x
            ans = mid
            high = mid - 1
    
    return ans


    
    

    
    
    