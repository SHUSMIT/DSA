def isValid(arr,cows,mid):
    count=1,last_placed = arr[0]
    for i in range(1,len(arr)):
        if arr[i] - last_placed >= mid:  ##distance consecutive is atleast greater than mid/min disance then only place the cow
            count += 1
            last_placed = arr[i]
        if count >= cows:
            return True
    return count>=cows


def cow_place(arr,cows):
    arr.sort()
    low,high = 1,max(arr)-min(arr)
    ans = high 
    while low<= high:
        mid = (low+high)//2
        if isValid(arr,cows,mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans