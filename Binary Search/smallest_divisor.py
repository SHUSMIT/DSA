import math
def isValid(arr,thres,mid):
    x = sum([math.ceil(x/mid) for x in arr])
    return x<=thres

def smallest_divisor(arr,thres):
    low,high = arr[0],arr[len(arr)-1]
    ans = high
    while low<=high:
        mid = (low+high)//2
        if isValid(arr,thres,mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
            