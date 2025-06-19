def isValid(arr,mid,paint):
    current = 0
    count = 1
    for i in range(len(arr)):
        if current + arr[i] <= mid: ##he can paint more
            current += arr[i] ##painter gets more allocated
        else:
            count += 1 ## go to next painter
            current = arr[i]
            
    return count

def painter_allocate(arr,paint):
    low,high = max(arr),sum(arr)
    ans = -1
    if paint > len(arr):
        return -1
    
    while low <=high:
        mid = (low+high)//2
        painter = isValid(arr,mid,paint)
        if painter <= paint: ## more has to be given to other painter so reduce
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
    