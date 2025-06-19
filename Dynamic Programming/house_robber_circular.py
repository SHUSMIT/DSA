def optimised(arr):    ### prev2  prev   curr
    prev = arr[0]         ### i-2     i-1     i 
    prev2 = 0

    for i in range(1,len(arr)):

        pick = arr[i]

        if i>1:
            pick += prev2
        
        not_pick = 0 + prev
        curr = max(pick,not_pick)

        prev2 = prev
        prev = curr
    
    return prev


def house_robber_circular(arr):
    
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]


    with_first = optimised(arr[:-1]) ## as first and last are conencted circular, so we take first and ignore last
    with_last = optimised(arr[1:]) ## similar
    return max(with_first,with_last)


arr = [2, 1, 4, 9]
n = len(arr)

print("Optimised:", house_robber_circular(arr))


