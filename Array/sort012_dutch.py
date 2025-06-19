def sort_012_dutch(arr):
    n = len(arr)
    low=0
    mid = 0
    high = n-1
    ## [0 to low-1] --> 0
    ## [low to mid -1] --> 1
    ## [mid to high] --> unsorted
    ## [high+1 to n-1] --> 2

    ## if a[mid] = 0 -> swap mid and low val and low,mid ++
    ## if a[mid] = 1 -> mid is in sroted but it should be in unsorted -> mid +1
    ## if a[mid] = 2 -> swap mid and high val and high --, mid not moved as the swapped one can be 0 also
    
    while mid < high:
        if arr[mid] == 0:
            arr[low] , arr[mid] = arr[mid], arr[low]
            low += 1
            mid +=1
        elif arr[mid] == 1:
            mid +=1 
        else:
            arr[high] , arr[mid] = arr[mid], arr[high]
    
    return arr
