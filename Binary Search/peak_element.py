def peak(arr,n):
    low,high = 1,n-2
    if n==1:
        return arr[0]
    ##edge case
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n-1] > arr[n-2]:
        return arr[n-1]
     
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return arr[mid]
        ##on the increasing half (/)
        elif arr[mid] < arr[mid+1] and arr[mid-1] < arr[mid]:
            low = mid + 1
        ##on decreasing half (\)
        else:
            high = mid - 1
    
    return -1