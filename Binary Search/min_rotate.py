def min_rotate(arr,target):
    low,high = 0,len(arr)-1
    ans = float('inf')
    while low<=high:
        mid = (low+high)//2
        ##left sorted
        if(arr[mid] >= arr[low]):
            ans = min(arr[low],ans)
            low = mid + 1
        else:
            ans = min(arr[mid],ans)
            high = mid - 1 
    return ans