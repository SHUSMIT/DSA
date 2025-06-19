def search_rotate(arr,target):
    low,high = 0,len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
            
        ##right sorted
        elif arr[low] > arr[mid]:
            if(arr[mid] < target and target <= arr[high]):
                low = mid + 1
            else:
                high = mid - 1
        ##left sorted
        else:
            if(arr[low] <= target and target < arr[mid]):
                high = mid - 1
            else:
                low = mid + 1
    return -1