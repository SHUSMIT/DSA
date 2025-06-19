def iter_bs(arr,target,n):
    low,high = 0,n-1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]==target):
            return mid
        elif(target > arr[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return -1 

def recur_bs(arr,low,high,target,n):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == target:
        return mid
    elif (arr[mid] < target):
        return recur_bs(arr,mid+1,high,target,n)
    else:
        return recur_bs(arr,low,mid-1,target,n)
            