def isValid(arr,d,mid):
    days = 1
    curr_capacity = 0
    
    for i in range(len(arr)):
        if mid >= curr_capacity + arr[i]: ## curr_capacity + weight is less so more can be stored
            curr_capacity += arr[i]
        else:
            days += 1
            curr_capacity = arr[i]  ##we re initialise with that capacity and continue in next day
            
    return days <= d

def ship_carry(arr,d):
    low,high = arr[len(arr)-1], sum(arr)
    ans = high
    while low<=high:
        mid = (low+high)//2
        if isValid(arr,d,mid):
            ans = mid
            high = mid - 1
            
        else:
            low = mid + 1
    return ans