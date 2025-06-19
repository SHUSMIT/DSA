def upper_bound(arr,x):
    low, high = 0, len(arr) - 1
    ans = high
    while low<=high:
        mid = (low+high)//2
        if arr[mid] > x:
            ans = mid
            high = mid - 1 ## i have got something that is atleast bigger so i shift to left half to find smaller
        else:
            low = mid + 1
    return ans         
    
def row_max1(mat):
    n = len(mat)
    m = len(mat[0])
    ## traverse each row and find number of 1, find max 1... keep counter variable
    ## first 1 can be found by lowerbund(1) or upperbound(0) and subtract that from m gives count
    count = 0
    index = -1
    
    for i in range(n):
        ones = m - upperbound(mat[i],0)
        if ones > count:
            count = ones
            index = i
            
    return index
    