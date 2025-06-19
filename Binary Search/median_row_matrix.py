def upperbound(arr,x,m):
    low,high=0,m-1
    index = 0
    while low<=high:
        mid = (low+high)//2
        if arr[mid] > x:
            index = mid
            high = mid - 1
        else:
            low = mid + 1
    return index
    
def blackbox(mat,mid,n,m):
    val = 0
    for i in range(n):
        val += upperbound(mat[i],mid,m)
    return val
    
def median_row(mat):
    n,m=len(mat),len(mat[0])
    low,high = min(x[0] for x in mat), max(x[n-1] for x in mat) ## minimum would be min(1st element in each row) similarly max
    req = (n*m)//2
    while low<=high:
        mid = (low+high)//2
        smaller_equals = blackbox(mat,mid,n,m) ## gives me number of elements less than mid
        if(smaller_equals <= req):
            low = mid + 1
        else:
            high = mid - 1
    return low