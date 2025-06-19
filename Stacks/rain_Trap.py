def right(arr):
    # get me the right max of each element
    n = len(arr)
    right_max = [-1 for _ in range(n)]

    right_max[n-1] = arr[n-1]
    
    for i in range(n-2,-1,-1):
        right_max[i] = max(right_max[i+1] , arr[i])

    return right_max

def left(arr):

    n = len(arr)
    left_max = [-1 for _ in range(n)]
    left_max[0] = arr[0]

    for i in range(1,len(arr)):
        left_max[i] = max(left_max[i-1],arr[i])  # curr element and prev max stored
    
    return left_max

def trap_rainwater(arr):

    right_max = right_max(arr)
    left_max = left_max(arr)

    total = 0

    for i in range(n):
        l = left_max[i]
        r = right_max[i]

        if l > arr[i] and r > arr[i]: # it should be between two top for logging
            total += min(l,r) - arr[i]
    
    return total
